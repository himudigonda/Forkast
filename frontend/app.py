import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="Forkast - AI Nutrition Assistant", layout="wide")

# Main UI Layout
st.title("🥦 Forkast: AI-Powered Nutrition Assistant")
st.write("Scan a barcode or enter manually to analyze food nutrition.")

# Two-column layout for Analysis & Chat
col1, col2 = st.columns([1.2, 1])  # Left panel (Analysis) | Right panel (Chat)

with col1:  # LEFT PANEL: Product Analysis
    barcode = st.text_input("Enter Barcode", placeholder="e.g., 737628064502")

    if st.button("🔍 Analyze Product") and barcode:
        with st.spinner("Fetching product data..."):
            response = requests.get(f"{BACKEND_URL}/product/{barcode}")
            product_data = response.json()
            
            if "error" in product_data:
                st.error("❌ Product not found. Try another barcode.")
            else:
                st.session_state["product_data"] = product_data
                st.success("✅ Product data retrieved!")

    if "product_data" in st.session_state:
        from components.product_display import show_product_info
        show_product_info(st.session_state["product_data"])

with col2:  # RIGHT PANEL: Chat Interface
    st.subheader("💬 Chat with AI")
    
    if "product_data" in st.session_state:
        from components.chat_interface import chat_with_product
        chat_with_product(st.session_state["product_data"], BACKEND_URL)
    else:
        st.info("🔍 Analyze a product first to start the chat.")
