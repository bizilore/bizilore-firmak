# Firmas de correo — Bizilore

Firmas de correo sencillas y consistentes para las cuentas de webmail de Bizilore (Roundcube / Dinahosting).

## Qué firma usa cada cuenta

| Cuenta | Firma a usar | Logo principal | Logo Hazitik |
|---|---|---|---|
| `bizijolas@bizilore.eus` | `firmas/bizijolas.html` | Bizijolas | Sí, siempre |
| Cualquier otra `@bizilore.eus` | `firmas/bizilore.html` | Bizilore | Sí, siempre |

El logo de **Hazitik Kooperatiba** aparece en todas las firmas (más pequeño, debajo del logo principal), porque Bizilore y Bizijolas forman parte de la cooperativa.

## Firmas ya generadas, listas para copiar

Todas las cuentas de `datos/cuentas.xlsx` ya tienen su firma generada en `firmas/cuentas/`. Solo tienes que abrir el archivo que corresponda y copiar su contenido tal cual en Roundcube (ver [instalación](#3-instalar-la-firma-en-roundcube)), sin sustituir nada.

| Cuenta | Archivo |
|---|---|
| `artezkaritza@bizilore.eus` | `firmas/cuentas/artezkaritza.html` |
| `bizijolas@bizilore.eus` | `firmas/cuentas/bizijolas.html` |
| `bizilore@bizilore.eus` (principal) | `firmas/cuentas/bizilore.html` |
| `bizilorelagunak@bizilore.eus` | `firmas/cuentas/bizilorelagunak.html` |
| `curriculum@bizilore.eus` | `firmas/cuentas/curriculum.html` |
| `ekonomia@bizilore.eus` | `firmas/cuentas/ekonomia.html` |
| `eskola@bizilore.eus` | `firmas/cuentas/eskola.html` |
| `formazioa@bizilore.eus` | `firmas/cuentas/formazioa.html` |
| `idazkaritza@bizilore.eus` | `firmas/cuentas/idazkaritza.html` |
| `komunikazioa@bizilore.eus` | `firmas/cuentas/komunikazioa.html` |
| `kukuherri.ge@bizilore.eus` | `firmas/cuentas/kukuherri.ge.html` |
| `oharrak@bizilore.eus` | `firmas/cuentas/oharrak.html` |
| `proiektuintegrala@bizilore.eus` | `firmas/cuentas/proiektuintegrala.html` |
| `sareak.hazitik@bizilore.eus` | `firmas/cuentas/sareak.hazitik.html` |
| `slaterpetxea@bizilore.eus` | `firmas/cuentas/slaterpetxea.html` |
| `taloak@bizilore.eus` | `firmas/cuentas/taloak.html` |
| `udalekuak@bizilore.eus` | `firmas/cuentas/udalekuak.html` |
| `zaintza@bizilore.eus` | `firmas/cuentas/zaintza.html` |

### Añadir o modificar una cuenta

1. Edita `datos/cuentas.xlsx` (añade una fila nueva, o corrige un teléfono/cargo/dirección existente). Columnas: `Cuenta`, `Nombre apellidos`, `Cargo`, `Teléfono`, `Dirección`, `URL INSTAGRAM`.
2. Ejecuta `python3 scripts/generar_firmas.py` — regenera todos los archivos de `firmas/cuentas/` a partir del Excel y de las plantillas base (`firmas/bizilore.html` / `firmas/bizijolas.html`). Las cuentas que empiezan por `bizijolas` usan la plantilla de Bizijolas; el resto, la de Bizilore.
3. Sube los cambios al repositorio.

## Estructura del repositorio

```
datos/              → datos/cuentas.xlsx, la fuente de verdad de nombre/cargo/teléfono por cuenta
firmas/             → plantillas base (bizilore.html, bizijolas.html) y firmas/cuentas/ con una firma ya rellenada por cuenta
logos/              → los 3 logotipos (bizilore.png, bizijolas.png, hazitik.png)
scripts/            → generar_firmas.py, regenera firmas/cuentas/ a partir del Excel
```

## 1. Añadir los logos

Sigue las instrucciones de [`logos/README.md`](logos/README.md) y sube ahí los 3 archivos con esos nombres exactos. Las plantillas ya apuntan a esas rutas, así que en cuanto estén subidos las firmas mostrarán las imágenes correctas sin tocar nada más.

**Importante:** las plantillas cargan las imágenes desde GitHub (`raw.githubusercontent.com`), lo cual requiere que el repositorio sea **público**. Si el repo es privado, esas URLs devuelven error y las imágenes aparecen rotas en cualquier sitio (Roundcube, un `.html` guardado en local, etc.). Para hacerlo público: en GitHub, entra en el repositorio → **Settings** → baja hasta **Danger Zone** → **Change visibility** → **Make public**, y confirma escribiendo el nombre del repositorio.

Es una solución rápida para empezar, pero para uso a largo plazo es más fiable alojar los logos en `bizilore.eus` (tu propio dominio) y apuntar ahí las URLs de `firmas/*.html` — así evitas depender de la disponibilidad de GitHub y de que algún filtro de correo bloquee esas URLs.

## 2. Personalizar la firma de una cuenta nueva (manual, sin pasar por el Excel)

Si necesitas una firma puntual sin tocar `datos/cuentas.xlsx`, abre el archivo HTML que corresponda (`firmas/bizilore.html` o `firmas/bizijolas.html`) y sustituye estos campos por los datos reales, borrando las llaves `{{ }}`:

- `{{NOMBRE APELLIDOS}}`
- `{{Cargo}}`
- `{{TELÉFONO}}`
- `{{Dirección}}`
- `{{URL_INSTAGRAM}}` / `{{URL_LINKEDIN}}` (si no aplica, borra esa línea/enlace)

## 3. Instalar la firma en Roundcube

1. Entra en el webmail y ve a **Configuración (⚙) → Identidades**.
2. Selecciona la identidad/cuenta de correo.
3. En la pestaña **Firma**, activa la casilla **"Firma HTML"** (si no la activas antes, el editor trata el HTML como texto plano).
4. En la barra del editor busca el botón de **código fuente** (icono `<>`) y ábrelo. Se abre una ventana/panel aparte.
5. Dentro de esa ventana, borra lo que haya y pega el HTML ya personalizado (el contenido completo del archivo).
6. Pulsa el botón de esa misma ventana para **cerrarla/aceptar** (según el tema puede llamarse "Actualizar", "Aceptar" u "OK" — no es el mismo botón que el paso 7).
7. Solo entonces pulsa el **Guardar** general de la página de Identidad.
8. Envíate un correo de prueba a ti mismo para comprobar que el logo carga bien y todo se ve correcto.

### Si el botón Guardar no responde

Es un síntoma típico de que el editor se ha quedado en un estado inconsistente al pegar el HTML. Prueba en este orden:

- Asegúrate de haber pulsado el botón de aceptar **dentro** de la ventana de código fuente antes de tocar el Guardar general (paso 6 y 7 no son el mismo botón).
- Refresca la página (sin guardar cambios a medias), vuelve a activar "Firma HTML" y repite el proceso desde cero.
- Prueba en otro navegador o en una ventana de incógnito, por si hay algo en caché bloqueando el editor.
- Abre las herramientas de desarrollador del navegador (F12 → pestaña "Consola") justo antes de pulsar Guardar; si aparece algún error en rojo, es la pista clave para identificar el problema.

## Notas de diseño

La firma se ha mantenido deliberadamente simple: logo + nombre/cargo + contacto básico + un enlace a cada red social, sin colores ni elementos añadidos, para que no resulte recargada. Si más adelante tenéis definido un color corporativo concreto, se puede aplicar como acento (por ejemplo en el enlace de la web o en la línea divisoria) editando el `style` correspondiente en los archivos de `firmas/`.
