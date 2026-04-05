import cv2
import os

# Definimos parámetros generales y variables de ruta.
# Se usa ruta dinámica referida al archivo para asegurar que el dataset vaya a `data/procesadas`.
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dataset_dir = os.path.join(base_dir, 'data', 'dataset')
nombre_persona = 'Bernardo_Bejarano' 
ruta_completa = os.path.join(dataset_dir, nombre_persona)
fotos_maximas = 400

# Aseguramos la existencia del directorio objetivo
if not os.path.exists(ruta_completa):
    os.makedirs(ruta_completa)
    print(f"Directorio creado: {ruta_completa}")

# Inicializamos el clasificador preentrenado de filtros de Haar de OpenCV
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

# Inicializamos la captura de video en el índice 0 (se mantiene CAP_DSHOW para evitar bloqueos)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("Error crítico: No hay dispositivo de video disponible en el índice 0.")
    exit()

contador = 0
print(f"Captura iniciada para la etiqueta '{nombre_persona}'.")

while True:
    # Leemos cada frame del flujo de video
    ret, frame = cap.read()
    if not ret:
        print("Error en el flujo de video.")
        break

    # Convertimos a escala de grises para optimizar la detección del modelo
    grises = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Identificamos las coordenadas de las caras en el frame actual iterando a baja escala
    rostros = face_cascade.detectMultiScale(grises, scaleFactor=1.3, minNeighbors=1)

    for (x, y, w, h) in rostros:
        # Trazamos una región de interés (ROI) referencial en la ventana
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 124, 124), 2)

        # Recortamos la ROI identificada
        rostro_recortado = frame[y:y+h, x:x+w]
        
        # Normalizamos la resolución de la muestra a 160x160 px
        rostro_redimensionado = cv2.resize(rostro_recortado, (160, 160))

        # Almacenamos la matriz procesada en nuestra base de datos local
        nombre_archivo = f"{ruta_completa}/rostro_{contador}.jpg"
        cv2.imwrite(nombre_archivo, rostro_redimensionado)
        
        contador += 1
        print(f"Progreso extracción: {contador}/{fotos_maximas}")

    # Renderizamos el feed de video para monitoreo del usuario
    cv2.imshow('Módulo de recolección de dataset', frame)

    # Condición de paro: extracción concluida o interrupción de usuario a través de ESC
    tecla = cv2.waitKey(1)
    if tecla == 27 or contador >= fotos_maximas:
        break

# Liberamos el hardware y procesos gráficos tomados por el sistema
print("Extracción procesada por completo.")
cap.release()
cv2.destroyAllWindows()
