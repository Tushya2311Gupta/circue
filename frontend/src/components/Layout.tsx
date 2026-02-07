import { ReactNode } from "react";
import { NavLink } from "react-router-dom";
import {
  Activity,
  BarChart3,
  Boxes,
  Cpu,
  Globe2,
  Leaf,
  Recycle,
  ShieldCheck,
  ShoppingBag,
} from "lucide-react";

const navItems = [
  { to: "/", label: "Executive Dashboard", icon: BarChart3 },
  { to: "/assets", label: "IT Asset Registry", icon: Boxes },
  { to: "/ai", label: "AI Optimization", icon: Cpu },
  { to: "/circular", label: "Circular Workflows", icon: Recycle },
  { to: "/marketplace", label: "Reuse Marketplace", icon: ShoppingBag },
  { to: "/partners", label: "Partner Directory", icon: Globe2 },
  { to: "/reports", label: "ESG & Net Zero", icon: ShieldCheck },
  { to: "/operations", label: "Operations", icon: Activity },
];

export function AppShell({ children }: { children: ReactNode }) {
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-icon">
            <Leaf size={20} />
          </div>
          <div>
            <div className="brand-title">Sustainable ITAM</div>
            <div className="brand-subtitle">Net Zero Control Center</div>
          </div>
        </div>
        <nav className="nav">
          {navItems.map((item) => {
            const Icon = item.icon;
            return (
              <NavLink key={item.to} to={item.to} className={({ isActive }) => (isActive ? "nav-link active" : "nav-link")}>
                <Icon size={18} />
                <span>{item.label}</span>
              </NavLink>
            );
          })}
        </nav>
        <div className="sidebar-footer">
          <div className="status-pill">
            <span className="dot" />
            Live ESG Telemetry
          </div>
        </div>
      </aside>
      <div className="main">
        <header className="topbar">
          <div>
            <div className="topbar-title">Sustainable IT Asset Management Platform</div>
            <div className="topbar-subtitle">Circular economy intelligence for enterprise IT</div>
          </div>
          <div className="topbar-actions">
            <button className="ghost">Download ESG Report</button>
            <button className="primary">Add Asset</button>
          </div>
        </header>
        <main className="content">{children}</main>
      </div>
    </div>
  );
}
