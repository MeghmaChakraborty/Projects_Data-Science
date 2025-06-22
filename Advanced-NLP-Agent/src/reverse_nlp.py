from .chatbot_response_gen import respond_to_prompt

def build_prompt(profile):
    base = "I am a customer and"
    if profile.get("employment_status") == "unemployed":
        base += " I lost my job"
    if profile.get("payment_history") == "late":
        base += " and missed several payments"
    if profile.get("medical_emergency"):
        base += " due to a recent medical emergency"
    if profile.get("loan_amount"):
        base += f" after taking a loan of ${profile['loan_amount']}"
    return base + "."

def generate_complaints(profiles):
    return [respond_to_prompt(build_prompt(p)) for p in profiles]
