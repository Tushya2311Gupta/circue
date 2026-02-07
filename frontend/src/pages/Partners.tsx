import { SectionHeader } from "../components/Cards";

const partners = [
  { name: "EcoCycle", type: "Recycler", rating: 4.8, certifications: "R2, ISO 14001" },
  { name: "GreenLoop", type: "Refurbisher", rating: 4.5, certifications: "e-Stewards" },
  { name: "TechBridge", type: "Donor", rating: 4.7, certifications: "Impact Verified" },
];

export default function Partners() {
  return (
    <div className="page">
      <SectionHeader title="Refurbisher & Recycler Directory" subtitle="Verified partners and compliance ratings." />
      <div className="grid cols-3">
        {partners.map((partner) => (
          <div key={partner.name} className="card">
            <div className="card-title">{partner.name}</div>
            <div className="card-subtitle">{partner.type}</div>
            <div className="card-metric">Compliance Rating: {partner.rating}</div>
            <div className="card-meta">Certifications: {partner.certifications}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
