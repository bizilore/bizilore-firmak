# Firmas de correo — Bizilore

Firmas de correo sencillas y consistentes para las cuentas de webmail de Bizilore (Roundcube / Dinahosting).

## Qué firma usa cada cuenta

| Cuenta | Firma a usar | Logo principal | Logo Hazitik |
|---|---|---|---|
| `bizijolas@bizilore.eus` | `firmas/bizijolas.html` | Bizijolas | Sí, siempre |
| Cualquier otra `@bizilore.eus` | `firmas/bizilore.html` | Bizilore | Sí, siempre |

El logo de **Hazitik Kooperatiba** aparece en todas las firmas (más pequeño, debajo del logo principal), porque Bizilore y Bizijolas forman parte de la cooperativa.

## Estructura del repositorio

```
firmas/     → plantillas HTML de firma, una por marca
logos/      → los 3 logotipos (bizilore.png, bizijolas.png, hazitik.png)
```

## 1. Añadir los logos

Sigue las instrucciones de [`logos/README.md`](logos/README.md) y sube ahí los 3 archivos con esos nombres exactos. Las plantillas ya apuntan a esas rutas, así que en cuanto estén subidos las firmas mostrarán las imágenes correctas sin tocar nada más.

**Importante:** las plantillas cargan las imágenes desde GitHub (`raw.githubusercontent.com`), lo cual requiere que el repositorio sea público. Es una solución rápida para empezar, pero para uso a largo plazo es más fiable alojar los logos en `bizilore.eus` (tu propio dominio) y apuntar ahí las URLs de `firmas/*.html` — así evitas depender de la disponibilidad de GitHub y de que algún filtro de correo bloquee esas URLs.

## 2. Personalizar la firma de cada persona

Abre el archivo HTML que corresponda (`firmas/bizilore.html` o `firmas/bizijolas.html`) y sustituye estos campos por los datos reales, borrando las llaves `{{ }}`:

- `{{NOMBRE APELLIDOS}}`
- `{{Cargo}}`
- `{{TELÉFONO}}`
- `{{Dirección}}`
- `{{URL_INSTAGRAM}}` / `{{URL_LINKEDIN}}` (si no aplica, borra esa línea/enlace)

## 3. Instalar la firma en Roundcube

1. Entra en el webmail y ve a **Configuración (⚙) → Identidades**.
2. Selecciona la identidad/cuenta de correo.
3. En la pestaña **Firma**, activa la casilla **"Firma HTML"**.
4. En la barra del editor busca el botón de **código fuente** (icono `<>`) y ábrelo.
5. Pega ahí el HTML ya personalizado (el contenido completo del archivo, sin el comentario de cabecera).
6. Cierra la vista de código fuente y pulsa **Guardar**.
7. Envíate un correo de prueba a ti mismo para comprobar que el logo carga bien y todo se ve correcto.

## Notas de diseño

La firma se ha mantenido deliberadamente simple: logo + nombre/cargo + contacto básico + un enlace a cada red social, sin colores ni elementos añadidos, para que no resulte recargada. Si más adelante tenéis definido un color corporativo concreto, se puede aplicar como acento (por ejemplo en el enlace de la web o en la línea divisoria) editando el `style` correspondiente en los archivos de `firmas/`.
