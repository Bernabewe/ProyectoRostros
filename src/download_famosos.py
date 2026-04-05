#############################################################################################
# Se eligió el dataset LFW (Labeled Faces in the Wild) por ser un estándar académico curado. 
# Esto garantiza el uso de fotografías reales de figuras públicas 
# y elimina el "ruido" de los buscadores (como imágenes de IA o dibujos), 
# asegurando un entrenamiento limpio y profesional.
#############################################################################################
import os
import cv2
import numpy as np
from sklearn.datasets import fetch_lfw_people

# Configuración de rutas relativas dentro del proyecto
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
preprocesadas_dir = os.path.join(base_dir, 'data', 'preprocesadas')

# Definimos el número de categorías de famosos requeridas
cantidad_famosos = 6

def obtener_famosos_reales():
    # Descarga el dataset académico (solo personas con al menos 70 fotos)
    print("Accediendo al dataset LFW (Fotos reales)...")
    lfw = fetch_lfw_people(min_faces_per_person=70, color=True, slice_=None)
    
    # Cuenta cuántas fotos tiene cada persona en el dataset
    counts = np.bincount(lfw.target)
    
    # Selecciona los índices de los 6 famosos con mayor cantidad de imágenes
    top_indices = np.argsort(counts)[-cantidad_famosos:][::-1]
    
    # Itera sobre los famosos seleccionados para extraer sus fotos
    for idx in top_indices:
        # Limpia el nombre para usarlo como carpeta (cambia espacios por guiones bajos)
        nombre = lfw.target_names[idx].replace(" ", "_")
        ruta_famoso = os.path.join(preprocesadas_dir, nombre)
        
        # Crea la carpeta de la categoría si no existe
        os.makedirs(ruta_famoso, exist_ok=True)
        
        # Localiza todas las imágenes pertenecientes a este famoso
        indices_persona = np.where(lfw.target == idx)[0]
        print(f"Extrayendo {len(indices_persona)} fotos reales de: {nombre}")
        
        # Guarda cada imagen individualmente en el almacenamiento local
        for i, img_idx in enumerate(indices_persona):
            img = lfw.images[img_idx]
            
            # Convierte la imagen de formato RGB (float 0-1) a BGR (uint8 0-255) para OpenCV
            img_bgr = cv2.cvtColor((img * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)
            
            # Escribe el archivo JPG en la carpeta correspondiente
            cv2.imwrite(os.path.join(ruta_famoso, f"real_{i}.jpg"), img_bgr)

if __name__ == "__main__":
    obtener_famosos_reales()