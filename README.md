🛡️ AI Cybersecurity Agent

An AI-powered cybersecurity web application that simulates real-time detection of phishing attacks and insider threats using behavioral analysis.
Built as a demo project for the Microsoft Hackathon – Cybersecurity Domain.

🚀 Problem Statement

As organizations become more digital and distributed, cybersecurity threats such as phishing, insider misuse, and suspicious logins are increasing.
Security teams need intelligent systems that can analyze activity patterns, assess risk levels, and recommend actions quickly.

This project demonstrates how AI-driven logic can help:

Protect sensitive data

Build digital trust

Support faster security decisions

💡 Solution Overview

The AI Cybersecurity Agent:

Analyzes simulated activity logs

Calculates a risk score

Classifies risk as Low / Medium / High

Provides a recommended action

Generates a downloadable security report

The application is designed as a lightweight, modular web app with a clear frontend–backend separation.

🧱 System Architecture
Frontend (HTML, CSS, JavaScript)
        ↓
FastAPI Backend (Python)
        ↓
Risk Analysis Engine

🧩 Features

🔍 Phishing attack detection

👤 Insider threat analysis

📊 Risk score & risk level classification

📄 Downloadable threat report

🎨 Professional UI with branding and visuals

🔁 Smooth navigation (Analyze → Result → Back)

🛠️ Tech Stack
Backend
    Python
    FastAPI
    Uvicorn

Frontend
    HTML
    CSS
    JavaScript

📁 Project Structure
cybersecurityapp/
│
├── backend.py
├── risk_engine.py
├── attack_data.py
├── requirements.txt
├── README.md
│
├── frontend/
│   ├── index.html
│   ├── result.html
│   ├── style.css
│   ├── script.js
│   └── images/
│       ├── security.png
│       └── logo.png

▶️ How to Run the Project
1️⃣ Start the Backend

Open Command Prompt in the project folder and run:

python -m uvicorn backend:app --host 127.0.0.1 --port 8000


You should see:

Uvicorn running on http://127.0.0.1:8000


⚠️ Keep this terminal open.

2️⃣ Open the Frontend

Go to frontend/

Open index.html in a browser

3️⃣ Use the App

Select a threat scenario

Click Analyze Threat

View the analysis result

Download the report

Use Back to return

📄 Sample Output

Risk Level: High

Risk Score: 70

Explanation: Suspicious email language and unusual login location

Recommended Action: Lock account and force password reset

🔒 Scope & Limitations

This is a demo application

Uses simulated data, not live organizational data

Designed to showcase concept, logic, and UI, not production deployment

🌱 Future Enhancements

Real-time log ingestion

User authentication

Role-based access

Cloud deployment (Azure)

Advanced AI/ML models

👩‍💻 Author

Charishma
DNR Engineering College
Built for Microsoft Hackathon – Cybersecurity Track

✅ Final Note

This project demonstrates how AI can assist cybersecurity teams by:

Reducing response time

Improving decision-making

Enhancing digital trust