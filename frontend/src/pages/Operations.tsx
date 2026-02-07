import { SectionHeader } from "../components/Cards";

const ops = [
  { team: "North America IT", utilization: "78%", idle: "12%", risk: "Medium" },
  { team: "EMEA Data Centers", utilization: "84%", idle: "8%", risk: "Low" },
  { team: "APAC Field Ops", utilization: "69%", idle: "19%", risk: "High" },
];

export default function Operations() {
  return (
    <div className="page">
      <SectionHeader title="Operational Insights" subtitle="Identify underutilized assets and risk hotspots." />
      <div className="card">
        <div className="table">
          <div className="table-row header">
            <div>Business Unit</div>
            <div>Utilization</div>
            <div>Idle Assets</div>
            <div>Waste Risk</div>
          </div>
          {ops.map((row) => (
            <div key={row.team} className="table-row">
              <div>{row.team}</div>
              <div>{row.utilization}</div>
              <div>{row.idle}</div>
              <div className="badge">{row.risk}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
