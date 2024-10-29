from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

class WasteManagementAI:
    def __init__(self):
        self.quantity_predictor = RandomForestRegressor()
        self.efficiency_predictor = RandomForestRegressor()
        self.scaler = StandardScaler()
        
    def predict_waste_quantity(self, farm_size, season, crop_type, historical_data):
        """Predict expected waste quantity for planning purposes"""
        features = self._prepare_features(farm_size, season, crop_type, historical_data)
        return self.quantity_predictor.predict(features)
    
    def recommend_treatment_method(self, waste_type, quantity, biodegradable):
        """Recommend optimal treatment method based on waste characteristics"""
        treatment_scores = {
            'COMPOST': self._calculate_compost_score(waste_type, quantity, biodegradable),
            'RECYCLAGE': self._calculate_recycling_score(waste_type, quantity),
            'INCINERATION': self._calculate_incineration_score(waste_type, quantity),
            'ENFOUISSEMENT': self._calculate_burial_score(waste_type, quantity)
        }
        return max(treatment_scores.items(), key=lambda x: x[1])
    
    def predict_treatment_efficiency(self, waste_type, method, quantity, conditions):
        """Predict treatment efficiency percentage"""
        features = self._prepare_efficiency_features(waste_type, method, quantity, conditions)
        return self.efficiency_predictor.predict(features)[0] 