import { useState } from "react";
import axios from "axios";

export default function ClientLogin() {
  const [form, setForm] = useState({
    email: "",
    password: ""
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await axios.post("http://localhost:8000/api/v1/auth/login", {
        ...form,
        role: "client"
      });
      alert("Client logged in successfully!");
    } catch (err) {
      alert("Client login failed");
    }
  };

  return (
    <div>
      <h2>Client Login</h2>
      <form onSubmit={handleSubmit}>
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
        <button type="submit">Login</button>
      </form>
    </div>
  );
}