import { SectionHeader } from "../components/Cards";

const reuseListings = [
  { id: "L-221", asset: "MacBook Pro 16", condition: "A-", status: "Available", location: "Austin" },
  { id: "L-222", asset: "Cisco 9300 Switch", condition: "B+", status: "Reserved", location: "Frankfurt" },
];

const donationPipeline = [
  { asset: "Lenovo ThinkPad T14", partner: "TechBridge", date: "2026-02-01", impact: "School lab" },
  { asset: "HP EliteDesk", partner: "CircularAid", date: "2026-01-18", impact: "Community center" },
];

const recycling = [
  { asset: "Dell R740", partner: "EcoCycle", certificate: "REC-9921", compliant: true },
  { asset: "Surface Pro 7", partner: "GreenLoop", certificate: "REC-9933", compliant: true },
];

export default function Circular() {
  return (
    <div className="page">
      <SectionHeader title="Circular Economy Workflows" subtitle="Reuse, donation, and compliant recycling orchestration." />
      <div className="grid cols-3">
        <div className="card">
          <SectionHeader title="Reuse Marketplace" subtitle="Internal listings ready to redeploy." />
          <ul className="list">
            {reuseListings.map((item) => (
              <li key={item.id}>
                <strong>{item.asset}</strong> · {item.condition} · {item.status} · {item.location}
              </li>
            ))}
          </ul>
        </div>
        <div className="card">
          <SectionHeader title="Donation Tracking" subtitle="Impact and compliance tracking." />
          <ul className="list">
            {donationPipeline.map((item) => (
              <li key={item.asset}>
                <strong>{item.asset}</strong> → {item.partner} ({item.date}) · {item.impact}
              </li>
            ))}
          </ul>
        </div>
        <div className="card">
          <SectionHeader title="E-waste Audit Trail" subtitle="Certified recycling and chain of custody." />
          <ul className="list">
            {recycling.map((item) => (
              <li key={item.asset}>
                <strong>{item.asset}</strong> → {item.partner} · {item.certificate}
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}
