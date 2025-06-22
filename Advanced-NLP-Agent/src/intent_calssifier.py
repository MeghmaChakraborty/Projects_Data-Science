from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from sklearn.preprocessing import MultiLabelBinarizer
from datasets import Dataset

def train_intent_classifier(df):
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
    mlb = MultiLabelBinarizer()
    y = mlb.fit_transform([[lbl] if lbl else [] for lbl in df["intent"]])
    df["label"] = y.tolist()
    ds = Dataset.from_pandas(df[["user_input", "label"]])
    ds = ds.map(lambda x: tokenizer(x["user_input"], truncation=True, padding=True), batched=True)
    ds.set_format("torch", columns=["input_ids", "attention_mask", "label"])
    model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=y.shape[1])
    trainer = Trainer(model=model, args=TrainingArguments("intent_output", per_device_train_batch_size=8, num_train_epochs=1), train_dataset=ds)
    trainer.train()
    return model
