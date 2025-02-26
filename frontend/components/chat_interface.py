import streamlit as st
import requests

def chat_with_product(product_data, backend_url):
    """
    Provides an interactive chat interface for users to ask questions about the product.
    """
    st.subheader("💬 Ask me about this product!")

    user_query = st.text_input("Your question", placeholder="e.g., Is this safe for diabetics?")

    if st.button("🤖 Ask AI"):
        if not user_query:
            st.warning("⚠️ Please enter a question.")
            return
        
        with st.spinner("Thinking..."):
            response = requests.post(f"{backend_url}/chat", json={
                "user_query": user_query,
                "barcode": product_data["barcode"]
            })

            chat_response = response.json().get("response", "❌ No response from AI.")
            st.success("✅ AI Response:")
            st.write(chat_response)
