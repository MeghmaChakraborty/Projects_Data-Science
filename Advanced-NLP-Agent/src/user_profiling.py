import matplotlib.pyplot as plt

def sentiment_profile(df):
    df["user_sentiment"].value_counts().plot(kind="bar", title="User Sentiment")
    plt.show()
