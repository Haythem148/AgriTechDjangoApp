import pandas as pd
import numpy as np

# Génération de données aléatoires
np.random.seed(42)
data = {
    "TypeDechet": np.random.choice(["Déchets verts", "Plastique", "Papier", "Métal", "Déchets ménagers", "Déchets de bois", "Carton", "Textiles", "Déchets alimentaires", "Verre", "Déchets organiques", "Plastique dur"], 3000),
    "Quantite": np.random.randint(10, 200, size=3000),
    "Biodegradable": np.random.choice([0, 1], size=3000),
    "Method": np.random.choice(["Compostage", "Recyclage", "Incinération", "Enfouissement"], 3000),
    "Temperature": np.random.uniform(15, 850, size=3000),
    "Humidity": np.random.uniform(10, 80, size=3000),
    "Efficacite": np.random.uniform(40, 90, size=3000)
}

# Création du DataFrame et sauvegarde en CSV
df = pd.DataFrame(data)
df.to_csv("waste_management_data.csv", index=False)
print("Fichier CSV généré avec succès.")
