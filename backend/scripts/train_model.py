import argparse
from datetime import datetime
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

FEATURES = [
    "raw_material_kg",
    "recycled_material_kg",
    "waste_kg",
    "energy_kwh",
    "water_liters",
    "machine_downtime_min",
    "production_volume_units",
    "material_recovery_rate",
    "circularity_score",
]
TARGET = "high_waste_flag"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="dataset/circular_economy_dataset.csv")
    parser.add_argument("--output", default="backend/models/waste_risk_rf.pkl")
    parser.add_argument("--version", default="rf-v1")
    parser.add_argument("--n-estimators", type=int, default=120)
    parser.add_argument("--max-depth", type=int, default=10)
    parser.add_argument("--sample", type=int, default=60000)
    args = parser.parse_args()

    data_path = Path(args.input)
    if not data_path.exists():
        raise FileNotFoundError(f"Dataset not found at {data_path}")

    df = pd.read_csv(data_path)
    df = df[FEATURES + [TARGET]].copy()
    df = df.replace([np.inf, -np.inf], np.nan).dropna()

    if args.sample and len(df) > args.sample:
        df = df.sample(args.sample, random_state=42)

    X = df[FEATURES]
    y = df[TARGET].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=args.n_estimators,
        random_state=42,
        max_depth=args.max_depth,
        class_weight="balanced_subsample",
        n_jobs=-1,
    )
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    metrics = {
        "accuracy": float(accuracy_score(y_test, preds)),
        "f1": float(f1_score(y_test, preds)),
    }

    payload = {
        "model": model,
        "feature_names": FEATURES,
        "model_version": args.version,
        "trained_at": datetime.utcnow().isoformat(),
        "metrics": metrics,
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(payload, output_path)

    print(f"Saved model to {output_path}")
    print(f"Metrics: {metrics}")


if __name__ == "__main__":
    main()
