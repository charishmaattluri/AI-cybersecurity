from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from risk_engine import analyze_phishing, analyze_insider

app = FastAPI()

# ✅ ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend access
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/phishing")
def phishing():
    return analyze_phishing()

@app.get("/insider")
def insider():
    return analyze_insider()
