def classify_risk(product_data):
    """
    Assigns a health risk classification (Green, Yellow, Red) based on nutrient levels.
    """
    sugar = product_data["nutrients"]["sugar"]
    sodium = product_data["nutrients"]["sodium"]
    fat = product_data["nutrients"]["fat"]
    additives = len(product_data["additives"])

    score = (sugar * 2) + (sodium * 1.5) + (fat * 1.8) + (additives * 3)

    if score < 20:
        return "Green ✅"
    elif 20 <= score < 50:
        return "Yellow ⚠️"
    else:
        return "Red 🚨"
