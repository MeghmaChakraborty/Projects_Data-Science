# Advanced NLP Agent on Bitext Dataset

**Dataset:**
Bitext Customer Support LLM Chatbot Training Dataset
Hosted on: Hugging Face
Format: Human-agent multi-turn dialogues with labeled intents

**Key Modules:**

Data Preprocessing (preprocess.py)

Extracts customer-agent dialogue pairs

Prepares dataframe for modeling

Intent Classification (intent_classifier.py)

Tokenizes user input using DistilBERT

Trains multi-label classifier (Hugging Face Transformers)

Handles imbalanced labels using MultiLabelBinarizer

Sentiment Analysis (sentiment_model.py)

Applies pretrained sentiment model (e.g., BERT)

Labels sentiment for customer and agent messages

User Profiling (user_profiling.py)

Visualizes sentiment trends

Can be extended with clustering or demographics

Summarization (summarizer.py)

Summarizes user-agent dialogues using BART

Chatbot Response Generation (chatbot_response_gen.py)

GPT-2 generation pipeline

Generates agent-style responses to customer prompts

Reverse NLP (reverse_nlp.py)

Builds GPT-2 prompts from structured risk profiles

Simulates realistic customer complaints

Useful for data augmentation in low-resource domains

**Example Use:**
You can run this end-to-end in Jupyter using:

from src.preprocess import load_and_process
df = load_and_process()

from src.intent_classifier import train_intent_classifier
model = train_intent_classifier(df)

**Setup**

Install all dependencies:

pip install -r requirements.txt

**Run**

Each module can be run independently or orchestrated in the notebook provided.

**Requirements**

Python 3.8+

HuggingFace Transformers

Datasets

Scikit-learn

PyTorch

Pandas

Matplotlib
