from transformers import pipeline

def generate_summaries(df):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    df["summary"] = df.apply(lambda row: summarizer(f"Customer: {row['user_input']} Agent: {row['agent_response']}", max_length=60, min_length=10)[0]['summary_text'], axis=1)
    return df
