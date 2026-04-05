import cv2
import os

# Configuración de las rutas de entrada (fotos originales) y salida (recortes)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_dir = os.path.join(base_dir, 'data', 'preprocesadas')
output_dir = os.path.join(base_dir, 'data', 'procesadas')

# Carga del clasificador preentrenado de OpenCV para detección frontal de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def procesar_dataset_real():
    # Recorre cada carpeta de celebridad en el directorio de preprocesadas
    for famoso in os.listdir(input_dir):
        path_in = os.path.join(input_dir, famoso)
        path_out = os.path.join(output_dir, famoso)
        
        # Filtra solo directorios y crea la carpeta de destino si no existe
        if not os.path.isdir(path_in): continue
        os.makedirs(path_out, exist_ok=True)

        print(f"Procesando recortes de: {famoso}")
        contador = 0
        
        # Procesa cada imagen descargada individualmente
        for img_name in os.listdir(path_in):
            img = cv2.imread(os.path.join(path_in, img_name))
            if img is None: continue

            # Convierte a escala de grises para optimizar la detección del algoritmo
            grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Detecta las coordenadas del rostro dentro de la imagen
            rostros = face_cascade.detectMultiScale(grises, 1.3, 5)

            for (x, y, w, h) in rostros:
                # Recorta el área del rostro y redimensiona exactamente a 160x160 px
                rostro = cv2.resize(img[y:y+h, x:x+w], (160, 160))
                
                # Guarda el rostro procesado con un nombre seriado
                cv2.imwrite(os.path.join(path_out, f"rostro_{contador}.jpg"), rostro)
                contador += 1
                
                # Procesa solo el primer rostro detectado para evitar ruido en fotos grupales
                break

if __name__ == "__main__":
    procesar_dataset_real()