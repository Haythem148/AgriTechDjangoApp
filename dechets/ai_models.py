import joblib
import os

class WasteManagementAI:
    def __init__(self):
        # Chargez les modèles et le scaler
        base_path = os.path.join(os.path.dirname(__file__), 'ai_models')
        self.method_model = joblib.load(os.path.join(base_path, "method_model.pkl"))
        self.efficiency_model = joblib.load(os.path.join(base_path, "efficiency_model.pkl"))
        self.scaler = joblib.load(os.path.join(base_path, "scaler.pkl"))

    def recommend_treatment_method(self, quantity, biodegradable, temperature, humidity):
        # Préparer les données d'entrée pour la méthode de traitement
        features = self.scaler.transform([[quantity, biodegradable, temperature, humidity]])
        return self.method_model.predict(features)[0]

    def predict_treatment_efficiency(self, quantity, biodegradable, temperature, humidity):
        # Préparer les données d'entrée pour l'efficacité
        features = self.scaler.transform([[quantity, biodegradable, temperature, humidity]])
        return self.efficiency_model.predict(features)[0]
