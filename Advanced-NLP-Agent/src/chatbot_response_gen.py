from transformers import pipeline

generator = pipeline("text-generation", model="gpt2", max_length=100)

def respond_to_prompt(prompt):
    return generator(prompt, num_return_sequences=1)[0]["generated_text"]
