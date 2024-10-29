from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
from datetime import datetime

class CropHealthPredictor:
    def __init__(self):
        # Main prediction model
        self.health_model = RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
        # Yield prediction model
        self.yield_model = GradientBoostingRegressor(
            n_estimators=100,
            learning_rate=0.1,
            random_state=42
        )
        self.scaler = StandardScaler()
    
    def prepare_features(self, crop):
        # Calculate days since planting
        days_planted = (datetime.now().date() - crop.planting_date).days
        
        features = pd.DataFrame({
            'water_requirements': [crop.water_requirements],
            'fertilizer_requirements': [crop.fertilizer_requirements],
            'days_planted': [days_planted],
            'growth_stage': [self.encode_growth_stage(crop.growth_stage)],
            'crop_type': [self.encode_crop_type(crop.crop_type)],
            'area': [float(crop.area)]
        })
        
        return self.scaler.fit_transform(features)
    
    def encode_growth_stage(self, stage):
        stages = {'SEEDLING': 0, 'VEGETATIVE': 1, 'FLOWERING': 2, 'FRUITING': 3, 'MATURE': 4}
        return stages.get(stage, 0)
    
    def encode_crop_type(self, crop_type):
        types = {'VEGETABLE': 0, 'FRUIT': 1, 'GRAIN': 2, 'OTHER': 3}
        return types.get(crop_type, 0)
    
    def predict_health(self, crop):
        # Transform features
        X = self.prepare_features(crop)
        
        # Simple prediction logic based on current health and growth stage
        base_health = crop.health
        stage_impact = {
            'SEEDLING': 5,
            'VEGETATIVE': 3,
            'FLOWERING': 0,
            'FRUITING': -2,
            'MATURE': -4
        }
        
        predicted_change = stage_impact.get(crop.growth_stage, 0)
        predicted_health = max(0, min(100, base_health + predicted_change))
        
        return round(predicted_health, 1)