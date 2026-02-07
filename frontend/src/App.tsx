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

// Auth Pages
import AdminLogin from "./pages/auth/AdminLogin";
import AdminRegister from "./pages/auth/AdminRegister";
import ClientLogin from "./pages/auth/ClientLogin";
import ClientRegister from "./pages/auth/ClientRegister";

export default function App() {
  return (
    <AppShell>
      <Routes>
        {/* Core App */}
        <Route path="/" element={<Dashboard />} />
        <Route path="/assets" element={<Assets />} />
        <Route path="/assets/:assetId" element={<AssetDetail />} />
        <Route path="/ai" element={<AiOptimization />} />
        <Route path="/circular" element={<Circular />} />
        <Route path="/marketplace" element={<Marketplace />} />
        <Route path="/partners" element={<Partners />} />
        <Route path="/reports" element={<Reports />} />
        <Route path="/operations" element={<Operations />} />

        {/* Admin Auth */}
        <Route path="/admin/login" element={<AdminLogin />} />
        <Route path="/admin/register" element={<AdminRegister />} />

        {/* Client Auth */}
        <Route path="/client/login" element={<ClientLogin />} />
        <Route path="/client/register" element={<ClientRegister />} />
      </Routes>
    </AppShell>
  );
}