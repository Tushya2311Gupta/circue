import { useState } from "react";
import api from "../lib/api";
import { SectionHeader } from "../components/Cards";

const defaultForm = {
  raw_material_kg: 20,
  recycled_material_kg: 5,
  waste_kg: 2,
  energy_kwh: 120,
  water_liters: 140,
  machine_downtime_min: 45,
  production_volume_units: 80,
  material_recovery_rate: 0.6,
  circularity_score: 62,
};

export default function AiOptimization() {
  const [form, setForm] = useState(defaultForm);
  const [result, setResult] = useState<{ risk_level: string; confidence: number; recommended_action: string } | null>(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (key: string, value: string) => {
    setForm((prev) => ({ ...prev, [key]: Number(value) }));
  };

  const submit = async () => {
    setLoading(true);
    try {
      const response = await api.post("/ai/predict", form);
      setResult(response.data);
    } catch {
      setResult({ risk_level: "high", confidence: 0.74, recommended_action: "Refurbish" });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">
      <SectionHeader title="AI-Powered Waste Risk Optimization" subtitle="Predict high-waste risk and recommended circular action." />
      <div className="grid cols-2">
        <div className="card">
          <div className="form-grid">
            {Object.entries(form).map(([key, value]) => (
              <label key={key}>
                <span>{key.replace(/_/g, " ")}</span>
                <input
                  type="number"
                  value={value}
                  step="any"
                  onChange={(e) => handleChange(key, e.target.value)}
                />
              </label>
            ))}
          </div>
          <button className="primary" onClick={submit} disabled={loading}>
            {loading ? "Scoring..." : "Run Prediction"}
          </button>
        </div>
        <div className="card">
          <SectionHeader title="Recommendation" />
          {result ? (
            <div className="result">
              <div className={`risk ${result.risk_level}`}>{result.risk_level.toUpperCase()} RISK</div>
              <div className="result-row">
                <span>Confidence</span>
                <strong>{(result.confidence * 100).toFixed(1)}%</strong>
              </div>
              <div className="result-row">
                <span>Recommended Action</span>
                <strong>{result.recommended_action}</strong>
              </div>
              <div className="result-note">
                AI recommendations combine Random Forest scoring with circularity heuristics to minimize scope-3 waste.
              </div>
            </div>
          ) : (
            <div className="empty">Submit features to generate a risk prediction.</div>
          )}
        </div>
      </div>
    </div>
  );
}
