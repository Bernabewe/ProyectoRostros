"""
Módulo para realizar Data Augmentation en los rostros.
- Rotación
- Brillo y contraste
- Espejo (Flip)
Usando la librería Albumentations.
"""

import cv2
import albumentations as A
import numpy as np

class FaceAugmenter:
    def __init__(self):
        """
        Define el pipeline de transformaciones usando Albumentations.
        """
        self.transform = A.Compose([
            A.HorizontalFlip(p=0.5), # Espejo
            A.RandomBrightnessContrast(p=0.2), # Brillo y contraste
            A.Rotate(limit=20, p=0.5), # Rotación
            # TODO: Añadir más aumentos si es necesario
        ])

    def augment_image(self, image):
        """
        Aplica las transformaciones a una imagen dada.
        Retorna la imagen aumentada.
        """
        augmented = self.transform(image=image)
        return augmented['image']

    def generate_augmented_dataset(self, source_dir, dest_dir, augmentations_per_image=5):
        """
        Aplica data augmentation a un directorio entero de imágenes recortadas.
        """
        # TODO: Leer imágenes del directorio origen y guardar múltiples versiones aumentadas
        pass

if __name__ == "__main__":
    # Prueba básica del módulo
    print("Módulo de aumento de datos cargado.")
