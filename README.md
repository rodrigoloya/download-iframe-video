# Download iframe video
Un script simple e interactivo en Python para descargar de forma nativa videos desde iframes de plataformas de streaming (como BunnyCDN o mediadelivery.net).

## Requisitos
* Tener [uv](https://github.com/astral-sh/uv) instalado.

## Uso
Ejecuta el script con `uv`:

```bash
uv run download.py
```

El script te preguntará la URL del video y se encargará de instalar su dependencia (`yt-dlp`) en un entorno virtual aislado en milésimas de segundo gracias a PEP 723 (Inline Script Metadata).

## Archivos descargados
Los videos se guardarán en esta misma carpeta en formato `.mp4` u otros de acuerdo a la mejor calidad provista por la URL, sin registrar la historia en tu control de versiones (git).
