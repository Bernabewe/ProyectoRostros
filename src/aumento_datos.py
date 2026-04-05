import cv2
import os
import numpy as np
import random
import shutil

# Configuración de directorios de entrada y salida final
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_dir = os.path.join(base_dir, 'data', 'procesadas')
output_dir = os.path.join(base_dir, 'data', 'dataset')
objetivo_fotos = 400

def aplicar_aumentacion(imagen):
    #Genera una variación visual de la imagen original
    opcion = random.choice(['espejo', 'brillo'])
    
    if opcion == 'espejo':
        # Volteo horizontal de la imagen
        return cv2.flip(imagen, 1)
    else:
        # Alteración aleatoria de la luminosidad en el canal V (HSV)
        factor = random.uniform(0.7, 1.3)
        hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV).astype(np.float64)
        hsv[:, :, 2] = np.clip(hsv[:, :, 2] * factor, 0, 255)
        return cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)

def construir_dataset():
    # Creación de la carpeta raíz del dataset final
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Procesamiento por cada categoría (alumno o famoso)
    for categoria in os.listdir(input_dir):
        ruta_in = os.path.join(input_dir, categoria)
        ruta_out = os.path.join(output_dir, categoria)
        
        if not os.path.isdir(ruta_in): continue
        if not os.path.exists(ruta_out): os.makedirs(ruta_out)

        # Filtrado de archivos de imagen válidos
        archivos_base = [f for f in os.listdir(ruta_in) if f.endswith(('.jpg', '.png'))]
        total_base = len(archivos_base)
        
        print(f"Procesando {categoria}: {total_base} originales encontradas.")

        # Paso 1: Copiar imágenes originales limitando el total a 400
        fotos_cargadas = []
        for i, nombre_archivo in enumerate(archivos_base):
            if i >= objetivo_fotos: 
                break

            img = cv2.imread(os.path.join(ruta_in, nombre_archivo))
            if img is None: continue
            
            cv2.imwrite(os.path.join(ruta_out, f"original_{i}.jpg"), img)
            fotos_cargadas.append(img)

        # Paso 2: Generar imágenes aumentadas si no se alcanzó el objetivo
        if total_base > 0:
            faltantes = objetivo_fotos - len(fotos_cargadas)
            for i in range(max(0, faltantes)):
                # Selecciona una foto procesada al azar para transformarla
                foto_base = random.choice(fotos_cargadas)
                nueva_img = aplicar_aumentacion(foto_base)
                cv2.imwrite(os.path.join(ruta_out, f"aumentada_{i}.jpg"), nueva_img)
            
            print(f"--- Finalizado: {categoria} tiene 400 imágenes en /dataset.")

if __name__ == "__main__":
    construir_dataset()