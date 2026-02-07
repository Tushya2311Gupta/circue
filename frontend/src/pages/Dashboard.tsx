import { Area, AreaChart, Bar, BarChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import { SectionHeader, StatCard } from "../components/Cards";

const emissionsData = [
  { month: "Jan", emissions: 1200, circularity: 62 },
  { month: "Feb", emissions: 1150, circularity: 64 },
  { month: "Mar", emissions: 980, circularity: 68 },
  { month: "Apr", emissions: 940, circularity: 71 },
  { month: "May", emissions: 880, circularity: 74 },
  { month: "Jun", emissions: 820, circularity: 77 },
];

const assetFlow = [
  { stage: "Purchase", value: 320 },
  { stage: "Use", value: 860 },
  { stage: "Repair", value: 140 },
  { stage: "Reuse", value: 210 },
  { stage: "Refurbish", value: 90 },
  { stage: "Recycle", value: 60 },
];

export default function Dashboard() {
  return (
    <div className="page">
      <SectionHeader
        title="Executive Sustainability Dashboard"
        subtitle="Scope-3 emissions, circularity uplift, and asset lifecycle health."
      />
      <div className="grid cols-4">
        <StatCard title="Assets Tracked" value="1,420" delta="+6.2% vs last quarter" />
        <StatCard title="Scope-3 Emissions" value="820 tCO2e" delta="-9.4% YoY" />
        <StatCard title="Circularity Index" value="77.3" delta="+12 pts" />
        <StatCard title="Waste Diverted" value="48.2 t" delta="+18%" />
      </div>

      <div className="grid cols-2">
        <div className="card">
          <SectionHeader title="Emissions & Circularity" subtitle="Monthly trend across IT asset lifecycle." />
          <div className="chart">
            <ResponsiveContainer width="100%" height={240}>
              <AreaChart data={emissionsData}>
                <XAxis dataKey="month" />
                <YAxis />
                <Tooltip />
                <Area type="monotone" dataKey="emissions" stroke="#1d4ed8" fill="#bfdbfe" />
                <Area type="monotone" dataKey="circularity" stroke="#059669" fill="#a7f3d0" />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>
        <div className="card">
          <SectionHeader title="Lifecycle Flow" subtitle="Current asset allocation by lifecycle stage." />
          <div className="chart">
            <ResponsiveContainer width="100%" height={240}>
              <BarChart data={assetFlow}>
                <XAxis dataKey="stage" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="value" fill="#0f766e" radius={[8, 8, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      <div className="grid cols-3">
        <div className="card">
          <SectionHeader title="Hotspots" subtitle="High-waste risk clusters." />
          <ul className="list">
            <li>Legacy laptops with <strong>low circularity</strong> in APAC</li>
            <li>Data center servers approaching <strong>end of lease</strong></li>
            <li>Peripheral inventory in <strong>idle state &gt; 90 days</strong></li>
          </ul>
        </div>
        <div className="card">
          <SectionHeader title="AI Recommendations" subtitle="Top actions reducing emissions." />
          <ul className="list">
            <li>Redeploy 46 devices to shared services pool</li>
            <li>Refurbish 18 servers for hybrid cloud migration</li>
            <li>Recycle 12 devices with compliant partners</li>
          </ul>
        </div>
        <div className="card">
          <SectionHeader title="SDG Alignment" subtitle="SDG-12 and SDG-17 indicators." />
          <div className="badge-grid">
            <div className="badge">
              <div className="badge-title">SDG-12</div>
              <div className="badge-value">0.82</div>
            </div>
            <div className="badge">
              <div className="badge-title">SDG-17</div>
              <div className="badge-value">0.64</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
