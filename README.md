# Predicción de Deserción Académica mediante Árbol de Decisión

Este repositorio contiene la implementación de un modelo de aprendizaje supervisado (**Árbol de Decisión**) diseñado para predecir la retención y el abandono estudiantil en el instituto tecnológico Beltran a partir de sus datos académicos, demográficos y socioeconómicos.

---

## 👥 Integrantes

* **Bautista Limer** 
* **Tomas Verniano** 
* **Dylan Velazquez Wooley** 
* **Leonel Encina** 

---

## ⚙️ Metodología y Modelo

1. **Cálculo de Entropía Inicial ($H(S)$):**
   * Evaluación de la impureza en el conjunto de entrenamiento comparando la proporción de alumnos que continúan sus estudios vs. los que abandonan.

2. **Preprocesamiento y Codificación:**
   * Eliminación/filtrado de variables no predictivas o sesgadas.
   * Codificación One-Hot Encoding (`get_dummies`) para transformar variables categóricas en binarias numéricas.
   * Alineación de columnas (`reindex`) entre los conjuntos de entrenamiento y prueba para garantizar consistencia dimensional.

3. **Entrenamiento del Árbol de Decisión:**
   * Algoritmo `DecisionTreeClassifier` con hiperparámetros de regularización (`max_depth=4`, `min_samples_split=20`) para evitar *overfitting* y garantizar la interpretabilidad del modelo.

4. **Inferencia y Visualización:**
   * Clasificación automática del estado final de nuevos alumnos (`Continúa` / `Abandonó`).
   * Renderizado gráfico del gráfico del árbol mediante `scikit-learn` y `matplotlib`.

---

## 🚀 Requisitos e Instalación

### Requisitos Previos

* Python 3.x
* Librerías requeridas: `pandas`, `scikit-learn`, `matplotlib`

Instalación de dependencias:

```bash
pip install pandas scikit-learn matplotlib
