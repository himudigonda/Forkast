import streamlit as st
import requests

def chat_with_product(product_data, backend_url):
    """
    Provides an interactive chat interface for users to ask questions about the product.
    """
    st.markdown("### 🤖 AI Chat Assistant")
    st.write("Ask questions about this product, its nutrition, and health impact.")

    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    user_query = st.text_input("Your question", placeholder="e.g., Is this safe for diabetics?")

    if st.button("🤖 Ask AI"):
        if not user_query:
            st.warning("⚠️ Please enter a question.")
            return
        
        with st.spinner("Thinking..."):
            payload = {
                "user_query": user_query,
                "barcode": product_data["barcode"],
                "user_id": None  # Optional user profile feature
            }

            response = requests.post(f"{backend_url}/chat", json=payload)
            
            if response.status_code != 200:
                st.error(f"❌ Chat failed! Error {response.status_code}: {response.text}")
                return

            ai_response = response.json().get("response", "❌ No response from AI.")

            # Store chat history
            st.session_state["chat_history"].append(("User", user_query))
            st.session_state["chat_history"].append(("AI", ai_response))

    # Display Chat History
    for role, text in st.session_state["chat_history"]:
        st.markdown(f"**{role}:** {text}")
