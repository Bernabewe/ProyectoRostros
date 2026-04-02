"""
Módulo para el preprocesamiento de imágenes de rostros.
- Detección y alineación con MTCNN
- Redimensionamiento a 160x160
- Normalización de píxeles
"""

import cv2
import numpy as np
from mtcnn import MTCNN

class FacePreprocessor:
    def __init__(self):
        self.detector = MTCNN()
        self.target_size = (160, 160)

    def detect_face(self, image):
        """
        Detecta el rostro en la imagen usando MTCNN.
        Devuelve las coordenadas del bounding box o None si no se detecta.
        """
        # TODO: Implementar la detección
        pass

    def crop_and_align(self, image, box, keypoints):
        """
        Recorta y alinea el rostro detectado.
        """
        # TODO: Implementar recorte y alineación
        pass

    def resize_and_normalize(self, face_image):
        """
        Redimensiona a 160x160 y normaliza los píxeles (por ejemplo, a [-1, 1] o [0, 1]).
        """
        # TODO: Implementar redimensionamiento y normalización
        pass

    def process_image(self, image_path):
        """
        Flujo completo de preprocesamiento para una imagen.
        """
        # 1. Leer imagen
        # 2. Detectar rostro
        # 3. Recortar y alinear
        # 4. Redimensionar y normalizar
        # 5. Devolver imagen preprocesada
        pass

if __name__ == "__main__":
    # Prueba básica del módulo
    print("Módulo de preprocesamiento cargado.")
