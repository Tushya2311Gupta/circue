import { Route, Routes } from "react-router-dom";
import { AppShell } from "./components/Layout";
import Dashboard from "./pages/Dashboard";
import Assets from "./pages/Assets";
import AssetDetail from "./pages/AssetDetail";
import AiOptimization from "./pages/AiOptimization";
import Circular from "./pages/Circular";
import Marketplace from "./pages/Marketplace";
import Partners from "./pages/Partners";
import Reports from "./pages/Reports";
import Operations from "./pages/Operations";

export default function App() {
  return (
    <AppShell>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/assets" element={<Assets />} />
        <Route path="/assets/:assetId" element={<AssetDetail />} />
        <Route path="/ai" element={<AiOptimization />} />
        <Route path="/circular" element={<Circular />} />
        <Route path="/marketplace" element={<Marketplace />} />
        <Route path="/partners" element={<Partners />} />
        <Route path="/reports" element={<Reports />} />
        <Route path="/operations" element={<Operations />} />
      </Routes>
    </AppShell>
  );
}
