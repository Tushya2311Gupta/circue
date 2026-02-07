-- PostgreSQL schema
CREATE TABLE users (
  id VARCHAR(36) PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  full_name VARCHAR(255) NOT NULL,
  hashed_password VARCHAR(255) NOT NULL,
  role VARCHAR(32) NOT NULL,
  is_active BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE assets (
  id VARCHAR(36) PRIMARY KEY,
  asset_tag VARCHAR(64) UNIQUE,
  name VARCHAR(255),
  category VARCHAR(32),
  manufacturer VARCHAR(255),
  model VARCHAR(255),
  purchase_date DATE,
  location VARCHAR(255),
  status VARCHAR(32),
  usage_hours FLOAT,
  energy_kwh FLOAT,
  waste_kg FLOAT,
  recycled_material_kg FLOAT,
  raw_material_kg FLOAT,
  water_liters FLOAT,
  circularity_score FLOAT,
  carbon_kg FLOAT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE lifecycle_events (
  id VARCHAR(36) PRIMARY KEY,
  asset_id VARCHAR(36) REFERENCES assets(id),
  event_type VARCHAR(32),
  event_date TIMESTAMP,
  details VARCHAR(1000),
  performed_by VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE prediction_logs (
  id VARCHAR(36) PRIMARY KEY,
  asset_id VARCHAR(36),
  input_features VARCHAR(2000),
  risk_level VARCHAR(16),
  confidence FLOAT,
  recommended_action VARCHAR(32),
  model_version VARCHAR(64),
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE esg_metrics (
  id VARCHAR(36) PRIMARY KEY,
  period_start DATE,
  period_end DATE,
  scope3_emissions_kg FLOAT,
  circularity_index FLOAT,
  waste_diverted_kg FLOAT,
  recycled_materials_kg FLOAT,
  sdg12_alignment FLOAT,
  sdg17_alignment FLOAT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE partners (
  id VARCHAR(36) PRIMARY KEY,
  name VARCHAR(255) UNIQUE,
  partner_type VARCHAR(32),
  contact_email VARCHAR(255),
  phone VARCHAR(64),
  address VARCHAR(500),
  certifications VARCHAR(1000),
  compliance_rating FLOAT,
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE marketplace_listings (
  id VARCHAR(36) PRIMARY KEY,
  asset_id VARCHAR(36) REFERENCES assets(id),
  listing_status VARCHAR(32),
  asking_price FLOAT,
  available_from TIMESTAMP,
  reserved_by VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE donation_records (
  id VARCHAR(36) PRIMARY KEY,
  asset_id VARCHAR(36) REFERENCES assets(id),
  partner_id VARCHAR(36) REFERENCES partners(id),
  donation_date TIMESTAMP,
  impact_notes VARCHAR(1000),
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE recycling_records (
  id VARCHAR(36) PRIMARY KEY,
  asset_id VARCHAR(36) REFERENCES assets(id),
  partner_id VARCHAR(36) REFERENCES partners(id),
  recycle_date TIMESTAMP,
  certificate_id VARCHAR(255),
  compliant BOOLEAN,
  created_at TIMESTAMP DEFAULT NOW()
);
