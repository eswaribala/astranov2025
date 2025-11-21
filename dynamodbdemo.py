from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from decimal import Decimal
import uuid
import boto3
from botocore.exceptions import ClientError
from typing import List

# ---------------------------
# DynamoDB Connection
# ---------------------------
dynamodb = boto3.resource(
    "dynamodb",
    region_name="us-east-1"      # Change if needed
)
table = dynamodb.Table("items")   # Table MUST exist


# ---------------------------
# Pydantic Models
# ---------------------------
class ItemIn(BaseModel):
    name: str
    price: float


class ItemOut(ItemIn):
    item_id: str


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
@app.post("/items", response_model=ItemOut)
def create_item(item: ItemIn):
    item_id = str(uuid.uuid4())

    db_item = {
        "item_id": item_id,
        "name": item.name,
        "price": Decimal(str(item.price))   # must use Decimal
    }

    try:
        table.put_item(Item=db_item)
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))

    return ItemOut(item_id=item_id, **item.dict())


# ----------------------------------------
# GET all items
# ----------------------------------------
@app.get("/items", response_model=List[ItemOut])
def get_items():
    try:
        response = table.scan()
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))

    items = response.get("Items", [])

    output = []
    for it in items:
        output.append(
            ItemOut(
                item_id=it["item_id"],
                name=it["name"],
                price=float(it["price"])  # convert Decimal → float
            )
        )
    return output


# ----------------------------------------
# GET item by ID
# ----------------------------------------
@app.get("/items/{item_id}", response_model=ItemOut)
def get_item(item_id: str):
    try:
        response = table.get_item(Key={"item_id": item_id})
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))

    if "Item" not in response:
        raise HTTPException(status_code=404, detail="Item not found")

    it = response["Item"]
    return ItemOut(
        item_id=it["item_id"],
        name=it["name"],
        price=float(it["price"])
    )
