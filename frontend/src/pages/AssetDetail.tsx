import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../lib/api";
import { SectionHeader } from "../components/Cards";
import type { Asset } from "../types/asset";

export default function AssetDetail() {
  const { assetId } = useParams();
  const [asset, setAsset] = useState<Asset | null>(null);

  useEffect(() => {
    if (!assetId) return;
    api
      .get(`/assets/${assetId}`)
      .then((res) => setAsset(res.data))
      .catch(() => setAsset(null));
  }, [assetId]);

  if (!asset) {
    return (
      <div className="page">
        <SectionHeader title="Asset Details" subtitle="Select an asset from the registry." />
        <div className="card">No asset data available.</div>
      </div>
    );
  }

  return (
    <div className="page">
      <SectionHeader title={`Asset ${asset.asset_tag}`} subtitle={asset.name} />
      <div className="grid cols-3">
        <div className="card">
          <div className="card-title">Lifecycle Status</div>
          <div className="card-metric">{asset.status}</div>
          <div className="card-meta">Location: {asset.location}</div>
        </div>
        <div className="card">
          <div className="card-title">Carbon Footprint</div>
          <div className="card-metric">{asset.carbon_kg.toFixed(1)} kg CO2e</div>
          <div className="card-meta">Energy: {asset.energy_kwh} kWh</div>
        </div>
        <div className="card">
          <div className="card-title">Circularity Score</div>
          <div className="card-metric">{asset.circularity_score.toFixed(0)}%</div>
          <div className="card-meta">Recycled materials: {asset.recycled_material_kg} kg</div>
        </div>
      </div>
    </div>
  );
}
