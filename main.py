from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/optimisation-atelier")
def optimiser_flux(commandes: int, stock_laiton_kg: float):
    # Logique d'optimisation automatisée
    df = pd.DataFrame({
        'Operation': ['Polissage', 'Soleillage', 'Galvanoplastie'],
        'Temps_Unitaire_min': [2.5, 1.2, 4.0]
    })
    
    temps_total = df['Temps_Unitaire_min'].sum() * commandes
    besoin_matiere = commandes * 0.015
    statut_stock = "Suffisant" if stock_laiton_kg >= besoin_matiere else "Rupture Imminente"
    
    return {
        "Temps_Production_Minutes": temps_total, 
        "Laiton_Requis_kg": besoin_matiere,
        "Alerte_Stock": statut_stock
    }
