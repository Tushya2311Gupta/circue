from math import isnan


def calculate_circularity_score(raw_material_kg: float, recycled_material_kg: float) -> float:
    if raw_material_kg <= 0:
        return 0.0
    score = (recycled_material_kg / raw_material_kg) * 100
    return max(0.0, min(100.0, score))


def calculate_carbon_kg(
    raw_material_kg: float,
    recycled_material_kg: float,
    energy_kwh: float,
    waste_kg: float,
    water_liters: float,
) -> float:
    embodied = raw_material_kg * 2.5
    energy = energy_kwh * 0.4
    waste = waste_kg * 1.5
    water = water_liters * 0.0003
    recycling_credit = recycled_material_kg * 1.2
    carbon = embodied + energy + waste + water - recycling_credit
    if isnan(carbon):
        return 0.0
    return max(0.0, carbon)
