#!/usr/bin/env python3
"""
Genera las firmas HTML de firmas/cuentas/ a partir de datos/cuentas.xlsx,
usando como base las plantillas de firmas/bizilore.html y firmas/bizijolas.html.

Uso: python3 scripts/generar_firmas.py
"""
import re
import sys
from pathlib import Path

import openpyxl

REPO_ROOT = Path(__file__).resolve().parent.parent
XLSX_PATH = REPO_ROOT / "datos" / "cuentas.xlsx"
PLANTILLA_BIZILORE = REPO_ROOT / "firmas" / "bizilore.html"
PLANTILLA_BIZIJOLAS = REPO_ROOT / "firmas" / "bizijolas.html"
SALIDA_DIR = REPO_ROOT / "firmas" / "cuentas"

PLACEHOLDERS = {
    "{{NOMBRE APELLIDOS}}": "Nombre apellidos",
    "{{Cargo}}": "Cargo",
    "{{TELÉFONO}}": "Teléfono",
    "{{Dirección}}": "Dirección",
    "{{URL_INSTAGRAM}}": "URL INSTAGRAM",
}

# Bloque de redes sociales de las plantillas base, con Instagram y LinkedIn.
# Como el Excel no trae LinkedIn, se sustituye por una versión solo con Instagram.
BLOQUE_SOCIAL_ORIGINAL = re.compile(
    r'\n\s*<div style="font-size:12px;color:#666666;margin-top:8px;">\n'
    r'\s*<a href="\{\{URL_INSTAGRAM\}\}"[^>]*>Instagram</a>\n'
    r"\s*&nbsp;·&nbsp;\n"
    r'\s*<a href="\{\{URL_LINKEDIN\}\}"[^>]*>LinkedIn</a>\n'
    r"\s*</div>\n"
)

BLOQUE_SOLO_INSTAGRAM = (
    '\n      <div style="font-size:12px;color:#666666;margin-top:8px;">\n'
    '        <a href="{{URL_INSTAGRAM}}" style="color:#666666;text-decoration:none;">Instagram</a>\n'
    "      </div>\n"
)


def cuenta_a_nombre_archivo(cuenta: str) -> str:
    local = cuenta.split("@", 1)[0].strip()
    local = local.split(" ", 1)[0]  # descarta anotaciones tipo "(principal)"
    return local


def cargar_filas():
    wb = openpyxl.load_workbook(XLSX_PATH, data_only=True)
    ws = wb.active
    filas = list(ws.iter_rows(values_only=True))
    cabecera, *datos = filas
    return [dict(zip(cabecera, fila)) for fila in datos]


def construir_plantilla(ruta: Path) -> str:
    contenido = ruta.read_text(encoding="utf-8")
    contenido, n = BLOQUE_SOCIAL_ORIGINAL.subn(BLOQUE_SOLO_INSTAGRAM, contenido)
    if n != 1:
        sys.exit(f"No se pudo localizar el bloque de redes sociales en {ruta}")
    return contenido


def rellenar(plantilla: str, fila: dict) -> str:
    salida = plantilla
    for marcador, columna in PLACEHOLDERS.items():
        valor = fila[columna]
        salida = salida.replace(marcador, str(valor))
    return salida


def main():
    plantilla_bizilore = construir_plantilla(PLANTILLA_BIZILORE)
    plantilla_bizijolas = construir_plantilla(PLANTILLA_BIZIJOLAS)

    SALIDA_DIR.mkdir(parents=True, exist_ok=True)
    generadas = []
    for fila in cargar_filas():
        cuenta = fila["Cuenta"]
        nombre_archivo = cuenta_a_nombre_archivo(cuenta)
        plantilla = plantilla_bizijolas if nombre_archivo == "bizijolas" else plantilla_bizilore
        html = rellenar(plantilla, fila)
        destino = SALIDA_DIR / f"{nombre_archivo}.html"
        destino.write_text(html, encoding="utf-8")
        generadas.append(destino.name)

    print(f"Generadas {len(generadas)} firmas en {SALIDA_DIR}:")
    for nombre in generadas:
        print(f"  - {nombre}")


if __name__ == "__main__":
    main()
