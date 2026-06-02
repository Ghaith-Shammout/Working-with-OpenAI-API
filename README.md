# 🤖 AI Assistant with OpenAI API (Python)

A simple command-line AI assistant built using Python and the OpenAI API.  
This project demonstrates how to integrate OpenAI models into an application, manage prompts, and build interactive conversations.

***

## 📌 Overview

This project was built as part of my learning journey in the **“Working with the OpenAI API”** course on DataCamp.

The assistant:

* Accepts user input from the terminal
* Sends requests to the OpenAI API
* Returns AI-generated responses
* Supports configurable parameters like temperature and token limits

***

## 🧠 Features

* ✅ Chat-based interaction (CLI chatbot)
* ✅ Custom system prompt (define AI behavior)
* ✅ Configurable settings via `.env` file
* ✅ Clean, modular Python structure
* ✅ Supports different OpenAI models

***

## 🛠️ Tech Stack

* Python 3.x
* OpenAI Python SDK
* python-dotenv

***

## 📁 Project Structure

```
.
├── main.py              # Entry point for the AI assistant
├── pyproject.toml      # Project configuration and dependencies
├── uv.lock             # Locked dependency versions (auto-generated)
├── .env                # Environment variables (not committed)
└── README.md           # Project documentation
```

***

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-assistant-openai.git
cd ai-assistant-openai
```

***

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

* Windows:

```bash
venv\Scripts\activate
```

* macOS/Linux:

```bash
source venv/bin/activate
```

***

### 3. Install dependencies

```bash
pip install openai python-dotenv
```

***

### 4. Configure environment variables

Create a `.env` file in the root directory:

```
OPENAI_API_ENDPOINT=your_api_endpoint
OPENAI_API_KEY=your_api_key_here
OPENAI_DEPLOYMENT_MODEL=gpt-4o-mini
OPENAI_MAX_COMPLETION_TOKENS=150
OPENAI_TEMPERATURE=0.7
```

⚠️ Important:

* Do NOT wrap values in quotes
* Keep your API key private

***

## ▶️ How to Run

Run the application:

```bash
python main.py
```

You will see:

```
AI Assistant (type 'exit' to quit)

What would you like to do?:
```

Type your question and press Enter.  
Type `exit` to quit the program.

***

## 💡 Example

```
What would you like to do?: Explain what an API is

Assistant: An API (Application Programming Interface) is a way for different software systems to communicate with each other...
```

## 📚 Learning Context

This project was created as part of:
**DataCamp – Working with the OpenAI API**

Key concepts applied:

* Prompt engineering
* Chat-based interactions
* API integration
* Parameter tuning (temperature, tokens)

***

## 👤 Author

@Ghaith Shammout  
AI Engineer

***
