class FarmRiskAnalyzer:
    def analyze_crop_risks(self, crop):
        risks = {
            'water_stress': self._calculate_water_stress(crop),
            'disease_risk': self._calculate_disease_risk(crop),
            'yield_risk': self._calculate_yield_risk(crop)
        }
        return risks
    
    def _calculate_water_stress(self, crop):
        # Convert Decimal to float for calculations
        water_req = float(crop.water_requirements)
        area = float(crop.area)
        
        # Calculate water stress based on requirements and conditions
        water_efficiency = water_req / area
        if water_efficiency > 100:
            return {'level': 'HIGH', 'score': 0.8}
        return {'level': 'LOW', 'score': 0.2}
    
    def _calculate_disease_risk(self, crop):
        # Calculate disease risk based on health history
        if crop.health < 50:
            return {'level': 'HIGH', 'score': 0.9}
        return {'level': 'LOW', 'score': 0.1}
        
    def _calculate_yield_risk(self, crop):
        # Calculate yield risk based on health and growth stage
        if crop.health < 50 or crop.growth_stage == 'SEEDLING':
            return {'level': 'HIGH', 'score': 0.9}
        elif crop.health < 70:
            return {'level': 'MEDIUM', 'score': 0.5}
        return {'level': 'LOW', 'score': 0.2}