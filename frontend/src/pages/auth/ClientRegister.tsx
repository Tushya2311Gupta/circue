import { useState } from "react";
import axios from "axios";

export default function ClientRegister() {
  const [form, setForm] = useState({
    company_name: "",
    email: "",
    password: ""
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await axios.post("http://localhost:8000/api/v1/auth/register", {
        full_name: form.company_name,
        email: form.email,
        password: form.password,
        role: "client"
      });
      alert("Client registered successfully!");
    } catch (err) {
      alert("Client registration failed");
    }
  };

  return (
    <div>
      <h2>Client Register</h2>
      <form onSubmit={handleSubmit}>
        <input
          name="company_name"
          placeholder="Company Name"
          value={form.company_name}
          onChange={handleChange}
          required
        />
        <input
          name="email"
          placeholder="Company Email"
          value={form.email}
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          value={form.password}
          onChange={handleChange}
          required
        />
        <button type="submit">Register</button>
      </form>
    </div>
  );
}