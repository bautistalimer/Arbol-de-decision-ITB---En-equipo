import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

#Entrenar
df_entrenamiento = pd.read_csv('TablaPrediccionAbandono-Entrenamiento.csv')

X_train = df_entrenamiento.drop(columns=['EstadoFinal', 'genero', 'carrera', 'trabaja/NoTrabaja', 'DistanciaDomicilioAlInstituto(Kms)', ])
y_train = df_entrenamiento['EstadoFinal']

X_train_encoded = pd.get_dummies(X_train, drop_first=True)

clf = DecisionTreeClassifier(max_depth=4, min_samples_split=20, random_state=42)
clf.fit(X_train_encoded, y_train)

#Probar
df_prueba = pd.read_csv('TablaPrediccionAbandono-DatosFinal.csv')

X_test = df_prueba.copy()

X_test_encoded = pd.get_dummies(X_test)

X_test_encoded = X_test_encoded.reindex(columns=X_train_encoded.columns, fill_value=0)

predicciones = clf.predict(X_test_encoded)

print("Predicciones:")
print(predicciones)

#Graficar
plt.figure(figsize=(10, 10)) 
plot_tree(
    clf,
    feature_names=X_train_encoded.columns,
    class_names=clf.classes_,
    filled=True,
    rounded=True,
    fontsize=8
        )
plt.title("Visualización del Árbol de Decisión - Predicción de Abandono", fontsize=14)
plt.show()