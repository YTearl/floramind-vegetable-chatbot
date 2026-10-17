"""
Fertilizer & Plot Calculator Router
Calculates precise NPK, organic compost, and commercial fertilizer dosage
based on crop, plot size in m², and growth stage.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

from app.data.vegetable_database import get_vegetable_by_id

router = APIRouter(prefix="/api/calculator", tags=["Calculator"])

# Standard baseline NPK requirements per hectare (kg/ha)
CROP_NPK_RATES = {
    "pechay": {"n": 100, "p": 60, "k": 60, "compost_tons_ha": 5.0},
    "ampalaya": {"n": 120, "p": 60, "k": 90, "compost_tons_ha": 8.0},
    "sitaw": {"n": 40, "p": 60, "k": 60, "compost_tons_ha": 4.0},
    "talong": {"n": 130, "p": 80, "k": 100, "compost_tons_ha": 8.0},
    "kalabasa": {"n": 90, "p": 60, "k": 90, "compost_tons_ha": 6.0},
    "kamatis": {"n": 120, "p": 80, "k": 120, "compost_tons_ha": 8.0},
    "okra": {"n": 70, "p": 50, "k": 60, "compost_tons_ha": 5.0},
    "sili": {"n": 110, "p": 70, "k": 90, "compost_tons_ha": 6.0},
    "kangkong": {"n": 90, "p": 40, "k": 50, "compost_tons_ha": 5.0},
    "repolyo": {"n": 150, "p": 90, "k": 120, "compost_tons_ha": 10.0},
    "carrots": {"n": 70, "p": 80, "k": 100, "compost_tons_ha": 5.0},
    "lettuce": {"n": 80, "p": 50, "k": 60, "compost_tons_ha": 6.0},
    "pipino": {"n": 100, "p": 60, "k": 90, "compost_tons_ha": 6.0},
    "labanos": {"n": 50, "p": 60, "k": 80, "compost_tons_ha": 4.0},
}

class FertilizerCalculationRequest(BaseModel):
    vegetable_id: str = Field(..., description="ID of the vegetable (e.g., pechay, kamatis)")
    area_sqm: float = Field(..., gt=0, description="Planting area in square meters (e.g. 50 m²)")
    soil_condition: Optional[str] = Field("medium", description="'low', 'medium', or 'rich'")

@router.post("/fertilizer")
async def calculate_fertilizer(req: FertilizerCalculationRequest):
    veg_id = req.vegetable_id.lower().strip()
    veg = get_vegetable_by_id(veg_id)
    if not veg:
        raise HTTPException(status_code=404, detail=f"Vegetable '{veg_id}' not found.")

    rates = CROP_NPK_RATES.get(veg_id, {"n": 90, "p": 60, "k": 70, "compost_tons_ha": 5.0})

    # Adjustment multiplier for soil fertility
    soil_mult = 1.0
    if req.soil_condition == "low":
        soil_mult = 1.25
    elif req.soil_condition == "rich":
        soil_mult = 0.75

    # 1 hectare = 10,000 sqm
    fraction_of_ha = req.area_sqm / 10000.0

    target_n = rates["n"] * soil_mult * fraction_of_ha
    target_p = rates["p"] * soil_mult * fraction_of_ha
    target_k = rates["k"] * soil_mult * fraction_of_ha
    compost_kg = (rates["compost_tons_ha"] * 1000.0) * fraction_of_ha

    # Inorganic Fertilizer Formulation:
    # 1. Complete (14-14-14): provides equal N, P, K.
    # We satisfy Phosphorus target using 14-14-14 as Basal (since P doesn't leach easily):
    # Complete needed (kg) = target_p / 0.14
    complete_14_kg = target_p / 0.14
    n_from_complete = complete_14_kg * 0.14
    k_from_complete = complete_14_kg * 0.14

    # 2. Remaining Nitrogen satisfied by Urea (46-0-0) as side-dress
    remaining_n = max(0.0, target_n - n_from_complete)
    urea_kg = remaining_n / 0.46

    # 3. Remaining Potassium satisfied by Muriate of Potash (0-0-60)
    remaining_k = max(0.0, target_k - k_from_complete)
    potash_0_0_60_kg = remaining_k / 0.60

    return {
        "vegetable": veg["name"],
        "scientific_name": veg["scientific_name"],
        "planting_area_sqm": req.area_sqm,
        "soil_fertility_level": req.soil_condition,
        "pure_nutrients_required_kg": {
            "nitrogen_n": round(target_n, 3),
            "phosphorus_p2o5": round(target_p, 3),
            "potassium_k2o": round(target_k, 3)
        },
        "recommended_materials": {
            "organic_compost_kg": round(compost_kg, 2),
            "complete_14_14_14_kg": round(complete_14_kg, 2),
            "urea_46_0_0_kg": round(urea_kg, 2),
            "potash_0_0_60_kg": round(potash_0_0_60_kg, 2)
        },
        "application_schedule": [
            {
                "stage": "Basal (At Land Preparation / 2-3 Days Before Planting)",
                "action": f"Incorporate {round(compost_kg, 2)} kg of well-rotted organic compost/vermicompost and {round(complete_14_kg, 2)} kg of Complete (14-14-14) thoroughly into the top 15 cm of soil.",
                "purpose": "Promotes root architecture, seedling anchorage, and gradual nutrient release."
            },
            {
                "stage": "Side-dress 1 (Early Vegetative: 12–15 Days After Transplanting / Emergence)",
                "action": f"Apply approximately {round(urea_kg * 0.5, 2)} kg of Urea (46-0-0) placed 5–8 cm away from the base of plants or dissolved in water (1 tbsp per 4 liters). Cover lightly with soil.",
                "purpose": "Boosts chlorophyll, foliage vigor, and rapid stem elongation."
            },
            {
                "stage": "Side-dress 2 (Flowering / Fruiting / Mid-Cycle)",
                "action": f"Apply {round(urea_kg * 0.5, 2)} kg Urea + {round(potash_0_0_60_kg, 2)} kg Muriate of Potash (0-0-60) along the rows. Water immediately after application.",
                "purpose": "Strengthens flower retention, enhances fruit sweetness, and prevents blossom drop."
            }
        ],
        "precautions": [
            "Never place raw synthetic fertilizer directly against the plant stem or foliage to prevent chemical leaf scorching.",
            "Always apply fertilizers when the soil is moist, or water deeply right after application.",
            "In high-rainfall tropical conditions, split side-dressing into smaller frequent doses to minimize leaching."
        ]
    }
