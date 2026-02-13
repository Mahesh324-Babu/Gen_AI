💰 AI-Powered Financial Data Analyzer
🌐 Overview

This project is an AI-driven financial data analysis application built using Streamlit and Google Gemini API.

It allows users to upload financial datasets (CSV, TXT, Excel), generate professional financial reports, and create AI-powered visualization code instantly.

The application focuses on structured analysis, business insights, and a clean, interactive UI — making it ideal for learning AI integration with data applications.

🚀 Features

📊 AI-generated Financial Analysis Reports

📁 Supports CSV, TXT, XLSX, XLS files

📈 AI-generated Matplotlib visualization code

🧠 Executive summary + business insights

🔐 Secure API key handling using environment variables

⚡ Fast and lightweight Streamlit interface

🧱 Modular multi-file architecture

🧱 Tech Stack

Python

Streamlit

Google Gemini API

Pandas

Matplotlib

python-dotenv

📂 Project Structure
financial-data-pro/
│
├── app.py                # Main Streamlit app
├── config.py             # API configuration
├── gemini_service.py     # Gemini model setup
├── file_handler.py       # File upload + processing
├── report_generator.py   # AI report generation
├── visualization.py      # AI visualization prompt
│
├── requirements.txt      # Dependencies
├── .env                  # API key (not shared)
└── README.md

⚙️ Installation
1️⃣ Clone the Repository
git clone <your-repository-link>
cd financial-data-pro

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv


Activate it:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

🔑 Environment Setup

Create a .env file inside the project folder and add your Gemini API key:

GOOGLE_API_KEY=your_api_key_here


⚠️ Do NOT upload .env to GitHub.

Add this to .gitignore:

.env
venv/

▶️ Run the Application
streamlit run app.py


After running, Streamlit will automatically open the app in your browser.

🧪 How It Works

User uploads a financial dataset.

The file is processed and converted into structured text.

A prompt is sent to the Gemini model.

The AI generates:

Executive summary

Revenue trends

Profitability insights

Risk factors

Recommendations

Optional: AI generates matplotlib visualization code.

⚠️ Notes

Do not upload your .env file to GitHub.

API usage may incur costs depending on your Gemini quota.

Large datasets may hit token limits.

AI-generated visualization code should be reviewed before execution.

📌 Future Improvements

Automatic chart rendering inside Streamlit

PDF export of financial reports

Advanced statistical analysis

Dashboard-style UI

SaaS deployment version

User authentication system
