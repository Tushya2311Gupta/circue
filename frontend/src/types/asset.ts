export interface Asset {
  id: string;
  asset_tag: string;
  name: string;
  category: string;
  status: string;
  location: string;
  energy_kwh: number;
  waste_kg: number;
  recycled_material_kg: number;
  raw_material_kg: number;
  circularity_score: number;
  carbon_kg: number;
}
