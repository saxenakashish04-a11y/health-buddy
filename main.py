from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="Health Buddy API", version="1.1.0")


class BMIRequest(BaseModel):
    height_cm: float = Field(..., gt=0, description="Height in centimeters")
    weight_kg: float = Field(..., gt=0, description="Weight in kilograms")


class SymptomCheckRequest(BaseModel):
    symptoms: List[str] = Field(
        ...,
        description="List of symptoms the user is experiencing",
        min_items=1,
    )


HEALTH_TIPS = [
    "Drink 2–3 liters of water daily.",
    "Aim for 7–9 hours of sleep each night.",
    "Include fruits and vegetables in every meal.",
    "Take short movement breaks every hour.",
    "Manage stress with breathing or short walks.",
]

SYMPTOM_LIBRARY = {
    "fever": {"possible_conditions": ["Common cold", "Flu"], "advice": "Rest, hydrate, monitor temperature."},
    "cough": {"possible_conditions": ["Common cold", "Flu", "Allergies"], "advice": "Use warm liquids; seek care if persistent."},
    "headache": {"possible_conditions": ["Tension headache", "Dehydration"], "advice": "Hydrate and rest; seek care if severe."},
    "fatigue": {"possible_conditions": ["Anemia", "Sleep deficiency", "Stress"], "advice": "Prioritize sleep and hydration."},
    "shortness of breath": {"possible_conditions": ["Asthma", "Respiratory infection"], "advice": "Seek medical care if worsening."},
}


def bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "underweight"
    if bmi < 25:
        return "normal"
    if bmi < 30:
        return "overweight"
    return "obese"


@app.get("/")
def home():
    return {"message": "Health Buddy is Live!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tips")
def get_tips():
    return {"tips": HEALTH_TIPS}


@app.post("/bmi")
def calculate_bmi(payload: BMIRequest):
    height_m = payload.height_cm / 100
    bmi = payload.weight_kg / (height_m**2)
    bmi_value = round(bmi, 2)
    return {"bmi": bmi_value, "category": bmi_category(bmi_value)}


@app.post("/symptoms/assess")
def assess_symptoms(payload: SymptomCheckRequest):
    normalized = [sym.lower() for sym in payload.symptoms]
    matched = []

    for symptom in normalized:
        info = SYMPTOM_LIBRARY.get(symptom)
        if info:
            matched.append({"symptom": symptom, **info})

    return {
        "matched": matched,
        "unrecognized": [sym for sym in normalized if sym not in SYMPTOM_LIBRARY],
        "disclaimer": "This is not medical advice. Consult a healthcare professional for diagnosis.",
    }
