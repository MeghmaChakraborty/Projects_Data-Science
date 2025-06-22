from transformers import pipeline

def apply_sentiment(df):
    sentiment_pipe = pipeline("sentiment-analysis")
    df["user_sentiment"] = df["user_input"].apply(lambda x: sentiment_pipe(x)[0]["label"])
    df["agent_sentiment"] = df["agent_response"].apply(lambda x: sentiment_pipe(x)[0]["label"])
    return df
