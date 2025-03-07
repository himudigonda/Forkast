from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional  # Import Optional for nullable fields
from api.product import fetch_product_data
from api.risk_scoring import classify_risk
from api.chatbot import chat_with_product
from api.user_profiles import get_user_profile
import uvicorn

app = FastAPI(title="Forkast API", description="AI-Powered Nutrition Assistant", version="1.0")

# Fix: Allow `user_id` to be `None`
class ChatRequest(BaseModel):
    user_query: str
    barcode: str
    user_id: Optional[str] = None  # ✅ Now user_id can be None

@app.get("/")
async def root():
    return {"message": "Welcome to Forkast - AI-Powered Nutrition Assistant"}

@app.get("/product/{barcode}")
async def get_product(barcode: str):
    """
    Fetch product data from Open Food Facts and classify risk levels.
    """
    product_data = fetch_product_data(barcode)
    if "error" in product_data:
        return {"error": "Product not found"}
    
    risk_score = classify_risk(product_data)
    product_data["risk_score"] = risk_score
    return product_data

@app.post("/chat")
async def chat_with_ai(request: ChatRequest):
    """
    Interact with the product chatbot powered by Ollama.
    """
    product_data = fetch_product_data(request.barcode)
    if "error" in product_data:
        raise HTTPException(status_code=404, detail="Product not found")
    
    user_profile = get_user_profile(request.user_id) if request.user_id else {}
    response = chat_with_product(request.user_query, product_data, user_profile)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
