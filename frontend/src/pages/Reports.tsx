import { useState } from "react";
import { SectionHeader } from "../components/Cards";

const apiBase = import.meta.env.VITE_API_URL || "http://localhost:8000/api/v1";

export default function Reports() {
  const [start, setStart] = useState("2026-01-01");
  const [end, setEnd] = useState("2026-02-06");
  const [format, setFormat] = useState("csv");

  const download = () => {
    const url = `${apiBase}/reports/esg?period_start=${start}&period_end=${end}&format=${format}`;
    window.open(url, "_blank");
  };

  return (
    <div className="page">
      <SectionHeader title="ESG & Net Zero Reporting" subtitle="Scope-3 dashboards, SDG alignment, and audit-ready exports." />
      <div className="grid cols-2">
        <div className="card">
          <SectionHeader title="Report Generator" subtitle="Export PDF or CSV for sustainability disclosures." />
          <div className="form-grid">
            <label>
              <span>Period Start</span>
              <input type="date" value={start} onChange={(e) => setStart(e.target.value)} />
            </label>
            <label>
              <span>Period End</span>
              <input type="date" value={end} onChange={(e) => setEnd(e.target.value)} />
            </label>
            <label>
              <span>Format</span>
              <select value={format} onChange={(e) => setFormat(e.target.value)}>
                <option value="csv">CSV</option>
                <option value="pdf">PDF</option>
              </select>
            </label>
          </div>
          <button className="primary" onClick={download}>Download Report</button>
        </div>
        <div className="card">
          <SectionHeader title="SDG Alignment" subtitle="Net Zero contribution by program." />
          <div className="sdg-grid">
            <div className="sdg-card">
              <div className="sdg-label">SDG-12</div>
              <div className="sdg-value">0.82</div>
              <div className="sdg-note">Responsible Consumption</div>
            </div>
            <div className="sdg-card">
              <div className="sdg-label">SDG-17</div>
              <div className="sdg-value">0.64</div>
              <div className="sdg-note">Partnerships for Goals</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
