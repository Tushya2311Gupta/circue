import { SectionHeader } from "../components/Cards";

const listings = [
  { id: "MK-101", asset: "Dell Latitude 5420", price: "$420", status: "Available" },
  { id: "MK-102", asset: "Cisco ISR 4451", price: "$980", status: "Reserved" },
  { id: "MK-103", asset: "HP ZBook", price: "$540", status: "Available" },
];

export default function Marketplace() {
  return (
    <div className="page">
      <SectionHeader title="Internal Reuse Marketplace" subtitle="Match idle assets with internal demand before procurement." />
      <div className="card">
        <div className="table">
          <div className="table-row header">
            <div>Listing</div>
            <div>Asset</div>
            <div>Price</div>
            <div>Status</div>
          </div>
          {listings.map((item) => (
            <div key={item.id} className="table-row">
              <div>{item.id}</div>
              <div>{item.asset}</div>
              <div>{item.price}</div>
              <div className="badge">{item.status}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
