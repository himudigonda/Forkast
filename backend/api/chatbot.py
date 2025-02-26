import subprocess
import json

OLLAMA_MODEL = "llama3.2:3b-instruct-q8_0"

def chat_with_product(user_query, product_data, user_profile):
    """
    Generates a response using the Ollama model based on product details and user input.
    """
    product_summary = f"""
    You are {product_data['name']} from {product_data['brand']}.
    Your nutrition breakdown per 100g: {product_data['nutrients']}
    You contain allergens: {product_data['allergens']}
    Your health classification: {product_data['nutri_score']}
    """

    prompt = f"""
    {product_summary}
    User has dietary preferences: {json.dumps(user_profile)}.
    User question: "{user_query}"
    Respond as if you are the product, in an engaging and informative way.
    """

    result = subprocess.run(["ollama", "run", OLLAMA_MODEL, prompt], capture_output=True, text=True)
    return result.stdout.strip()
