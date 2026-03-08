# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "yt-dlp",
# ]
# ///

import yt_dlp
import sys

def download_video(url):
    print(f"Preparando la descarga del video: {url}")
    
    # Opciones de configuración para yt-dlp
    ydl_opts = {
        # Guardaremos el video con en formato "video_<id>.<extension>"
        'outtmpl': 'video_descargado_%(id)s.%(ext)s', 
        
        # Descargar la mejor calidad disponible (video + audio)
        'format': 'bestvideo+bestaudio/best',
        
        # Simulamos ser un navegador (User-Agent) e incluimos el Referer
        # Las plataformas como mediadelivery/BunnyCDN a veces verifican esto.
        'http_headers': {
            'Referer': url,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n¡Descarga completada exitosamente!")
    except Exception as e:
        print(f"\nOcurrió un error al intentar descargar el video:\n{e}")
        sys.exit(1)

if __name__ == "__main__":
    print("-" * 50)
    print("🎬 Bienvenido al Descargador de Videos 🎬")
    print("-" * 50)
    print("Por favor, introduce la URL del video que deseas descargar.")
    print("Ejemplo: https://iframe.mediadelivery.net/play/...")
    print("Para salir, escribe 'salir' o presiona Ctrl+C.\n")
    
    while True:
        try:
            url_del_video = input("🔗 URL del video: ").strip()
            
            if url_del_video.lower() in ['salir', 'exit', 'quit']:
                print("¡Hasta luego 👋!")
                break
                
            if not url_del_video:
                print("❌ La URL no puede estar vacía. Inténtalo de nuevo.\n")
                continue
                
            if not url_del_video.startswith('http'):
                print("❌ La URL debe comenzar con http:// o https://\n")
                continue
                
            print("\n⚙️  Iniciando proceso...")
            download_video(url_del_video)
            print("\n✨ ¿Quieres descargar otro video? (Ingresa otra URL o escribe 'salir')")
            
        except KeyboardInterrupt:
            # Captura Ctrl+C para salir limpiamente
            print("\n\n¡Hasta luego 👋!")
            break
