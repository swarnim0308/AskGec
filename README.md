# AskGec - College Inquiry Chatbot

AskGec is an intelligent chatbot designed to facilitate students with instant responses to college-related queries. It leverages a pre-trained **BERT (Bidirectional Encoder Representations from Transformers)** model to understand natural language and generate context-aware answers from a custom knowledge base.

The application is built using **PyTorch** and **Flask**, featuring a responsive web interface with auto-detection for CUDA GPU / CPU environments.

## 🚀 Features

-   **Context-Aware AI**: Uses a fine-tuned BERT model (or fallback to `bert-base-uncased`) to understand and answer questions based on context.
-   **CPU & CUDA Auto-Detection**: Dynamically runs on GPU if available, or seamlessly falls back to CPU execution.
-   **Custom Knowledge Base**: Easily updatable `knowledgebase.txt` to provide specific information about the college.
-   **Web Interface**: Clean and responsive chat interface built with HTML, CSS, JavaScript, and jQuery.
-   **Local & Ngrok Deployment**: Runs out-of-the-box on `http://127.0.0.1:5000`, with optional Ngrok tunneling support (`USE_NGROK=1`).

## 🛠️ Tech Stack

-   **Backend**: Python, Flask
-   **AI/ML**: PyTorch, Transformers (BERT)
-   **Frontend**: HTML, CSS, JavaScript, jQuery
-   **Tunneling (Optional)**: Ngrok

## 📂 Project Structure

-   `server.py`: Main Flask server entry point.
-   `modeling.py`: BERT model architecture & device-agnostic tensor operations.
-   `infer.py`: Model inference & prediction pipeline with fallback handling.
-   `infer_utils.py`: Preprocessing utilities and feature conversion routines.
-   `knowledgebase.txt`: Text file containing the college context used for Q&A.
-   `static/`: Frontend assets (HTML template, CSS styles, JavaScript).

## 🔧 Installation & Usage

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/swarnim0308/AskGec.git
    cd AskGec
    ```

2.  **Install Dependencies**
    Ensure you have Python installed. You will need the following packages:
    ```bash
    pip install flask torch transformers pytorch-pretrained-bert
    ```
    *(Optional for tunneling)*: `pip install flask-ngrok`

3.  **Update Knowledge Base**
    Edit `knowledgebase.txt` with the context/information you want your chatbot to answer from.

4.  **Run the Local Web Application**
    ```bash
    python server.py
    ```
    Open your browser and navigate to **[http://127.0.0.1:5000](http://127.0.0.1:5000)**.

5.  **(Optional) Run with Ngrok Tunneling**
    To expose your local instance to the web via Ngrok:
    ```bash
    set USE_NGROK=1   # Windows Command Prompt
    # or $env:USE_NGROK="1" (PowerShell) / export USE_NGROK=1 (Linux/macOS)
    python server.py
    ```

## 🧠 How It Works

1.  The server reads `knowledgebase.txt` to build the context for the college.
2.  When a user submits a question via the chat interface, an HTTP POST request is sent to the Flask backend.
3.  The `InferCoQA` model (in `infer.py`) tokenizes the question alongside the context.
4.  The model computes start and end logit spans across tokens to extract the most accurate answer from the context.
5.  The answer is returned as JSON to the frontend chat UI.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

