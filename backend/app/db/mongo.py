from pymongo import MongoClient
from app.core.config import get_settings

settings = get_settings()

client = MongoClient(settings.MONGO_URI)
db = client.get_default_database()

circular_data_collection = db["circular_inputs"]
