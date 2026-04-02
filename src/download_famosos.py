from bing_image_downloader import downloader
import os

# 1. Definir los 6 famosos (puedes cambiarlos)
famosos = [
    "Lionel Messi", 
    "Taylor Swift", 
    "Elon Musk", 
    "Scarlett Johansson", 
    "Robert Downey Jr", 
    "Salma Hayek"
]

# 2. Ruta de destino
output_dir = "data/01_raw"

# 3. Bucle de descarga
for personaje in famosos:
    print(f"Descargando imágenes de: {personaje}...")
    downloader.download(
        personaje, 
        limit=30,  # Cantidad de fotos
        output_dir=output_dir, 
        adult_filter_off=True, 
        force_replace=False, 
        timeout=60,
        verbose=False
    )
    
    # 4. Renombrar carpeta para quitar espacios si es necesario
    folder_name = personaje.replace(" ", "_")
    old_path = os.path.join(output_dir, personaje)
    new_path = os.path.join(output_dir, folder_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)

print("¡Descarga completada!")