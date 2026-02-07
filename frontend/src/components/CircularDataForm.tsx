import { useState } from "react";
import { submitCircularData } from "../services/api.js";

const initialState = {
  production_volume_units: "",
  raw_material_kg: "",
  recycled_material_kg: "",
  energy_kwh: "",
  water_liters: "",
  machine_downtime_min: "",
  material_recovery_rate: "",
  circularity_score: ""
};

export default function CircularDataForm() {
  const [form, setForm] = useState(initialState);
  const [loading, setLoading] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      await submitCircularData({
        production_volume_units: Number(form.production_volume_units),
        raw_material_kg: Number(form.raw_material_kg),
        recycled_material_kg: Number(form.recycled_material_kg),
        energy_kwh: Number(form.energy_kwh),
        water_liters: Number(form.water_liters),
        machine_downtime_min: Number(form.machine_downtime_min),
        material_recovery_rate: Number(form.material_recovery_rate),
        circularity_score: Number(form.circularity_score)
      });

      alert("Data submitted successfully!");
      setForm(initialState);
    } catch (err) {
      alert("Submission failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {Object.keys(form).map((field) => (
        <input
          key={field}
          name={field}
          value={form[field as keyof typeof form]}
          onChange={handleChange}
          placeholder={field.replaceAll("_", " ")}
          required
        />
      ))}
      <button type="submit" disabled={loading}>
        {loading ? "Submitting..." : "Submit"}
      </button>
    </form>
  );
}
