# Claude Text Generation App (Streamlit + Bedrock)

This project is a secure and interactive text generation app using **Amazon Bedrock's Claude 3 model** and **Streamlit**. Designed for coursework or demo purposes, the app supports:

- Real-time text generation via AWS Bedrock
- API Key validation
- Prompt content filtering
- Usage logging to a local file
- Easy-to-run interface with Streamlit

---

## Demo

<img src="docs/Claude_Text_Generator.gif" width="1000"/>

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/claude-streamlit-app.git
cd claude-streamlit-app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

Copy the example:

```bash
cp .env.example .env
```

Then update it with your AWS credentials and API key.

### 4. Run the app

```bash
streamlit run app.py
```

---

## Features

- **Claude 3 via BedrockChat**
- **API key validation** via `.env`
- **Prompt filtering** for safe input
- **Local logging** in `usage_log.txt`
- **Modular design** for easy AWS deployment

---

## Project Structure

```
├── app.py
├── .env.example
├── requirements.txt
├── usage_log.txt
└── README.md
```

---

## Disclaimer

This app is intended for educational or demo use. Never commit your actual `.env` file or credentials to GitHub.

