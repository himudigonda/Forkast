# Forkast - AI-Powered Nutrition Assistant

Forkast is an AI-powered tool that allows users to scan food products, retrieve nutritional data from Open Food Facts, and chat with an AI-powered assistant that explains the product’s health impact.

### Features:
- **Barcode Input**: Enter or scan a barcode to retrieve product information.
- **Nutritional Breakdown**: Fetch data from Open Food Facts API.
- **AI Chatbot**: Engage with an LLM-powered chatbot that explains the product's impact.

### Running the Project:
1. **Install Dependencies**:
    ```bash
    pip install -r backend/requirements.txt
    pip install -r frontend/requirements.txt
    ```
2. **Run Backend (FastAPI)**:
    ```bash
    python backend/main.py
    ```
3. **Ensure Ollama Model is Installed**:
    ```bash
    ollama pull llama3.2:3b-instruct-q8_0
    ```
4. **Run Frontend (Streamlit)**:
    ```bash
    streamlit run frontend/app.py
    ```
