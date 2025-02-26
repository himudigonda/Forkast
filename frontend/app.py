import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="Forkast - AI Nutrition Assistant", layout="wide")

st.title("🥦 Forkast: AI-Powered Nutrition Assistant")
st.write("Scan a barcode or enter manually to analyze food nutrition.")

barcode = st.text_input("Enter Barcode", placeholder="e.g., 737628064502")

if st.button("🔍 Analyze Product") and barcode:
    response = requests.get(f"{BACKEND_URL}/product/{barcode}")
    product_data = response.json()
    
    if "error" in product_data:
        st.error("❌ Product not found.")
    else:
        st.session_state["product_data"] = product_data
        st.success("✅ Product data retrieved!")

if "product_data" in st.session_state:
    from components.product_display import show_product_info
    show_product_info(st.session_state["product_data"])
