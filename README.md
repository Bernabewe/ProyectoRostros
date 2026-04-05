# ProyectoRostros: Pipeline de Dataset Facial

Este repositorio contiene las herramientas necesarias para construir un dataset de reconocimiento facial desde cero, combinando capturas locales, descarga de datos académicos y técnicas de aumentación de datos para balancear las clases.

---

## 📁 Estructura de `/data`

El flujo de datos se organiza en tres etapas clave para mantener la integridad de las imágenes:

- **/preprocesadas**:  
  Contiene las imágenes de famosos "en bruto" (fotos completas) descargadas directamente del dataset LFW.

- **/procesadas**:  
  Almacena exclusivamente los rostros recortados (160x160 px) detectados tanto de las fotos de famosos como de las capturas locales.

- **/dataset**:  
  Es el repositorio final que contiene el set de datos equilibrado de 400 imágenes por persona, listo para el entrenamiento del modelo.

---

## ⚙️ Módulos Principales (`.py`)

El flujo de trabajo sigue este orden lógico de ejecución:

### 1. `captura_rostros.py` (Adquisición Local)

- **Función**:  
  Utiliza la cámara web para detectar y recortar tu rostro en tiempo real mediante Haar Cascades.

- **Detalle**:  
  Normaliza las capturas a una resolución de **160x160 px**.

- **Resultado**:  
  Almacena las muestras directamente en `data/dataset` bajo tu nombre de usuario.

---

### 2. `download_famosos.py` (Adquisición Externa)

- **Función**:  
  Descarga fotos reales de celebridades utilizando el dataset académico LFW (*Labeled Faces in the Wild*).

- **Detalle**:  
  Selecciona automáticamente a los 6 famosos con mayor cantidad de muestras disponibles.

- **Resultado**:  
  Guarda las fotos originales en la carpeta `data/preprocesadas`.

---

### 3. `procesar_famosos.py` (Limpieza de Datos)

- **Función**:  
  Toma las fotos de `data/preprocesadas` y extrae únicamente la región de interés (el rostro).

- **Detalle**:  
  Redimensiona cada recorte exactamente a **160x160 px** para mantener la consistencia del dataset.

- **Resultado**:  
  Exporta los rostros limpios a la carpeta `data/procesadas`.

---

### 4. `aumento_datos.py` (Optimización y Balanceo)

- **Función**:  
  Garantiza que cada categoría (tú y los famosos) alcance el objetivo de **400 imágenes**.

- **Técnica**:  
  Si el número de originales es insuficiente, genera nuevas versiones aplicando:
  - Espejo horizontal  
  - Variaciones de brillo aleatorias en el canal HSV  

- **Resultado**:  
  Genera el set final consolidado en `data/dataset`.

---

## 🚀 Flujo de Ejecución Recomendado

```bash
# Capturar tu Rostro
python src/captura_rostros.py

# Obtener Famosos
python src/download_famosos.py 

# Recortar Famosos
python src/procesar_famosos.py 

# Balancear Dataset
python src/aumento_datos.py 
