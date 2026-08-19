# AskGec - College Inquiry Chatbot 🤖

AskGec is an intelligent, context-aware chatbot designed to provide instant answers to college-related queries. It leverages a pre-trained **BERT (Bidirectional Encoder Representations from Transformers)** model to understand natural language questions and extract precise answers from a custom college knowledge base (`knowledgebase.txt`).

Built with **PyTorch** and **Flask**, AskGec supports dynamic **CPU and CUDA GPU auto-detection**, seamless local web deployment, and a hybrid model-fallback safety pipeline to ensure highly reliable responses.

---

## ✨ Features

- 🧠 **BERT-Powered Neural Inference**: Runs PyTorch BERT tokenization and logit span prediction (`BertForQuestionAnswering`) on every query.
- 🛡️ **Hybrid Model Fallback Guard**: Combines neural model span predictions with an intelligent sentence-matching fallback to prevent empty or un-tuned model responses.
- ⚡ **CPU & CUDA Auto-Detection**: Automatically detects hardware capabilities and seamlessly executes on NVIDIA CUDA GPUs or CPU fallback.
- 📝 **Customizable Knowledge Base**: Simply update `knowledgebase.txt` to train the bot on any college context or information without retraining.
- 🌐 **Responsive Web Interface**: Features an interactive HTML/CSS/JavaScript chat interface.
- 🔌 **Flexible Server Runner**: Runs out-of-the-box locally on `http://127.0.0.1:5000` with optional Ngrok public tunneling (`USE_NGROK=1`).

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend Framework** | Python 3.x, Flask |
| **Deep Learning Engine** | PyTorch, HuggingFace Transformers, PyTorch-Pretrained-BERT |
| **Frontend UI** | HTML5, CSS3, JavaScript, jQuery |
| **Tunneling (Optional)** | Flask-Ngrok |

---

## 📂 Project Structure

```
AskGec/
├── server.py             # Flask Web Application & API Entry Point
├── infer.py              # PyTorch BERT Inference Pipeline & Fallback Guard
├── infer_utils.py        # Tokenization, Feature Conversion & CoQA Data Structs
├── modeling.py           # BERT Neural Network Architecture & Device Management
├── knowledgebase.txt     # Plaintext Knowledge Context for College Q&A
├── requirements.txt      # Python Project Dependencies
├── .gitignore            # Git Ignore Rules
└── static/               # Frontend Web Assets (HTML, CSS, JS)
```

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/swarnim0308/AskGec.git
cd AskGec
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
*(Optional for Ngrok tunneling support)*:
```bash
pip install flask-ngrok
```

### 3. Run the Local Web Server
```bash
python server.py
```
Open your browser and navigate to:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## ⚙️ Configuration & Environment Variables

| Variable | Description | Default | Example |
| :--- | :--- | :--- | :--- |
| `USE_NGROK` | Set to `1` to enable public Ngrok tunneling | `0` (Local host only) | `set USE_NGROK=1` (Windows CMD) <br> `$env:USE_NGROK="1"` (PowerShell) |

To enable Ngrok tunneling:
```bash
# Windows PowerShell
$env:USE_NGROK="1"
python server.py
```

---

## 📄 Customizing Knowledge Base (`knowledgebase.txt`)

To update the chatbot's knowledge base:
1. Open `knowledgebase.txt`.
2. Format facts into **clear, line-separated sentences** (one sentence per line works best to prevent sequence truncation during BERT tokenization).
3. Save the file. The server reloads context on startup!

---

## 🔄 API Endpoint Reference

### `POST /`

Processes a user question and returns the extracted answer text.

**Request Form Data (`application/x-www-form-urlencoded`):**
| Parameter | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| `ques` | String | The question asked by the user | **Yes** |
| `prev_q` | String | Previous question in context (optional) | No |
| `prev_a` | String | Previous answer in context (optional) | No |

**Response:**
```text
The current principal of the college is Dr. BS Chawla.
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to open a Pull Request.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
