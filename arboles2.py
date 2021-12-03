# Importar bibliotecas
import pandas as pd
import numpy as np
#Importar conjunto de datos
dataset = pd.read_csv("C:/Users/stalyn/Downloads/matriz_fin.csv")
dataset.head()
#Preparación de datos para la formación
#El siguiente código divide los datos en atributos y etiquetas:
X = dataset.iloc[:, 0:17].values
y = dataset.iloc[:, 18].values
#Escala de funciones
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

# Feature Scaling
#escala nuestros datos
#Para hacerlo, usaremos Scikit-Learn’s StandardScaler clase. Ejecute el siguiente código para hacerlo:
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Entrenamiento del algoritmo
#Ahora que hemos escalado nuestro conjunto de datos,
#es hora de entrenar nuestro algoritmo de bosque aleatorio para resolver este problema de regresión
from sklearn.ensemble import RandomForestRegressor
import joblib
regressor = RandomForestRegressor(n_estimators=20, random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print('y pred',y_pred)
filename = 'arbol_5.pkl'
joblib.dump(regressor, filename)
# for i in range(100):
# 	print(y_pred[i], y_test[i])

#Evaluación del algoritmo
#Para los problemas de clasificación, las métricas que se utilizan para evaluar un algoritmo son la precisión, la matriz de confusión, la recuperación de precisión 
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print("Matriz de Confusion")
print(confusion_matrix(y_test,y_pred.round()))
print(classification_report(y_test,y_pred.round()))
print("acuracy : ", accuracy_score(y_test, y_pred.round()))
