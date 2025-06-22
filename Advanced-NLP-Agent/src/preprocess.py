import pandas as pd
from datasets import load_dataset

def load_and_process():
    dataset = load_dataset("bitext/Bitext-customer-support-llm-chatbot-training-dataset", split="train")
    pairs = []
    for d in dataset:
        lines = d["dialogue"].split("\n")
        for i in range(len(lines)-1):
            if lines[i].lower().startswith("customer:") and lines[i+1].lower().startswith("agent:"):
                u = lines[i].split(":",1)[1].strip()
                a = lines[i+1].split(":",1)[1].strip()
                pairs.append({"user_input": u, "agent_response": a, "intent": d.get("intent", "")})
    return pd.DataFrame(pairs)
