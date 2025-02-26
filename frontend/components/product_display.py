import streamlit as st

def show_product_info(product_data):
    """
    Displays product details and health classification in the UI.
    """
    st.subheader(f"🛒 {product_data['name']} ({product_data['brand']})")
    st.image(product_data["image"], width=150)

    st.markdown(f"**Nutritional Information per 100g:**")
    st.text(f"Sugar: {product_data['nutrients']['sugar']}g")
    st.text(f"Fat: {product_data['nutrients']['fat']}g")
    st.text(f"Sodium: {product_data['nutrients']['sodium']}mg")
    st.text(f"Calories: {product_data['nutrients']['calories']} kcal")

    st.markdown(f"**🔬 Additives:** {', '.join(product_data['additives']) if product_data['additives'] else 'None'}")
    st.markdown(f"**⚠️ Allergens:** {', '.join(product_data['allergens']) if product_data['allergens'] else 'None'}")

    # Display risk classification
    risk_label = product_data["risk_score"]
    st.markdown(f"### **Health Risk Classification: {risk_label}**")

    # Alternative suggestions (placeholder for now)
    st.markdown("💡 *Looking for healthier alternatives?* Coming soon! 🚀")
