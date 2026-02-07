from fastapi import APIRouter, HTTPException
from app.models.circular_input import CircularInput
from app.db.mongo import circular_data_collection
from app.services.csv_writer import write_to_csv

router = APIRouter(prefix="/api/ingest", tags=["Data Ingestion"])


@router.post("/circular-data")
async def ingest_circular_data(data: CircularInput):
    payload = data.model_dump()

    try:
        circular_data_collection.insert_one(payload)
        write_to_csv(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "status": "success",
        "message": "Data saved successfully"
    }
