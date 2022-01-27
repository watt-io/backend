from datetime import datetime
from typing import Dict
from fastapi import FastAPI

app = FastAPI()

@app.get("/health/")
def alive() -> Dict[str, datetime]:
    return {"timestamp": datetime.now()}