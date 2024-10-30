import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, mean_absolute_error
import joblib

# Charger les données depuis le CSV
data = pd.read_csv("data/waste_management_data.csv")

# Séparer les caractéristiques (features) et les cibles (targets)
X = data[['Quantite', 'Biodegradable', 'Temperature', 'Humidity']]
y_method = data['Method']
y_efficiency = data['Efficacite']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train_method, y_test_method = train_test_split(X, y_method, test_size=0.2, random_state=42)
X_train_eff, X_test_eff, y_train_eff, y_test_eff = train_test_split(X, y_efficiency, test_size=0.2, random_state=42)

# Standardiser les données
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_train_eff = scaler.fit_transform(X_train_eff)
X_test_eff = scaler.transform(X_test_eff)

# Entraîner le modèle pour la méthode de traitement
method_model = RandomForestClassifier(n_estimators=100, random_state=42)
method_model.fit(X_train, y_train_method)

# Entraîner le modèle pour l'efficacité
efficiency_model = RandomForestRegressor(n_estimators=100, random_state=42)
efficiency_model.fit(X_train_eff, y_train_eff)

# Évaluer les modèles
accuracy = accuracy_score(y_test_method, method_model.predict(X_test))
mae = mean_absolute_error(y_test_eff, efficiency_model.predict(X_test_eff))
print(f"Précision de la recommandation de méthode : {accuracy:.2f}")
print(f"Erreur moyenne absolue d'efficacité : {mae:.2f}")

# Sauvegarder les modèles et le scaler
joblib.dump(method_model, "method_model.pkl")
joblib.dump(efficiency_model, "efficiency_model.pkl")
joblib.dump(scaler, "scaler.pkl")
