from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from decimal import Decimal
import uuid
import boto3
from botocore.exceptions import ClientError
from typing import List
import uvicorn
# ---------------------------
# DynamoDB Connection
# ---------------------------
dynamodb = boto3.resource(
    "dynamodb",
    region_name="us-east-1"      # Change if needed
)
table = dynamodb.Table("regions")   # Table MUST exist


# ---------------------------
# Pydantic Models
# ---------------------------
class RegionIn(BaseModel):
    region_code: str
    name: str


class RegionOut(RegionIn):
    region_code: str
    name: str


# ---------------------------
# FastAPI app
# ---------------------------
app = FastAPI(title="Minimal Items API")


@app.get("/health")
def health():
    return {"status": "ok"}


# ----------------------------------------
# CREATE item
# ----------------------------------------
@app.post("/regions", response_model=RegionOut)
def create_region(region: RegionIn):
    region.region_code = str(uuid.uuid4())

    db_item = {
        "region_code": region.region_code,
        "name": region.name,
    }
    

    try:
        table.put_item(Item=db_item)
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))

    return RegionOut(region_code=region.region_code, name=region.name)


# ----------------------------------------
# GET all items
# ----------------------------------------
@app.get("/regions", response_model=List[RegionOut])
def get_regions():
    try:
        response = table.scan()
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))

    regions = response.get("Regions", [])

    output = []
    for it in regions:
        output.append(
            RegionOut(
                region_code=it["region_code"],
                name=it["name"]
            )
        )
    return output


if __name__ == "__main__":
    
    uvicorn.run(app, host="127.0.0.1", port=8000)