import requests
from config import OFF_API_URL

def fetch_product_data(barcode: str):
    """
    Fetch product data from Open Food Facts API and normalize the response.
    """
    url = OFF_API_URL.format(barcode=barcode)
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": "Product not found"}
    
    data = response.json().get("product", {})

    return {
        "barcode": barcode,
        "name": data.get("product_name", "Unknown Product"),
        "brand": data.get("brands", "Unknown Brand"),
        "nutrients": {
            "sugar": data["nutriments"].get("sugars_100g", 0),
            "fat": data["nutriments"].get("fat_100g", 0),
            "sodium": data["nutriments"].get("sodium_100g", 0),
            "calories": data["nutriments"].get("energy-kcal_100g", 0)
        },
        "ingredients": data.get("ingredients_text", "Unknown"),
        "additives": data.get("additives_tags", []),
        "allergens": data.get("allergens_tags", []),
        "nutri_score": data.get("nutriscore_grade", "Unknown"),
        "nova_group": data.get("nova_group", "Unknown"),
        "eco_score": data.get("ecoscore_grade", "Unknown"),
        "image": data.get("image_front_url", ""),
    }
