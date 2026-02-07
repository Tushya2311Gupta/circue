import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from "../lib/api";
import { SectionHeader } from "../components/Cards";
import type { Asset } from "../types/asset";

const fallbackAssets: Asset[] = [
  {
    id: "1",
    asset_tag: "LT-2291",
    name: "Dell Latitude 7420",
    category: "laptop",
    status: "in_use",
    location: "New York",
    energy_kwh: 112,
    waste_kg: 4.2,
    recycled_material_kg: 1.1,
    raw_material_kg: 8.7,
    circularity_score: 62,
    carbon_kg: 24.6,
  },
  {
    id: "2",
    asset_tag: "SV-9921",
    name: "HPE ProLiant DL380",
    category: "server",
    status: "repair",
    location: "London",
    energy_kwh: 620,
    waste_kg: 18.3,
    recycled_material_kg: 8.2,
    raw_material_kg: 42.5,
    circularity_score: 54,
    carbon_kg: 215.3,
  },
];

export default function Assets() {
  const [assets, setAssets] = useState<Asset[]>(fallbackAssets);

  useEffect(() => {
    api
      .get<Asset[]>("/assets")
      .then((res) => setAssets(res.data))
      .catch(() => setAssets(fallbackAssets));
  }, []);

  return (
    <div className="page">
      <SectionHeader title="IT Asset Registry" subtitle="Track lifecycle, emissions, and circularity at asset level." />
      <div className="card">
        <div className="table">
          <div className="table-row header">
            <div>Asset Tag</div>
            <div>Name</div>
            <div>Category</div>
            <div>Status</div>
            <div>Location</div>
            <div>Carbon (kg)</div>
            <div>Circularity</div>
          </div>
          {assets.map((asset) => (
            <div key={asset.id} className="table-row">
              <div>
                <Link to={`/assets/${asset.id}`}>{asset.asset_tag}</Link>
              </div>
              <div>{asset.name}</div>
              <div className="badge">{asset.category}</div>
              <div>{asset.status}</div>
              <div>{asset.location}</div>
              <div>{asset.carbon_kg.toFixed(1)}</div>
              <div>{asset.circularity_score.toFixed(0)}%</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
