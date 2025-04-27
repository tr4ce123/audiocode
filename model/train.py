from transformers import T5ForConditionalGeneration, T5Tokenizer, Trainer, TrainingArguments, EarlyStoppingCallback
from datasets import Dataset
import pandas as pd

df = pd.read_csv("./model/training_data_fixed.csv", quotechar='"')

dataset = Dataset.from_pandas(df)
dataset = dataset.train_test_split(test_size=0.1, seed=42)
train_dataset = dataset["train"]
eval_dataset = dataset["test"]

print(train_dataset)
print(eval_dataset)

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-small")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-small")

def preprocess_function(examples):
    inputs = ["translate instruction to code: " + instr for instr in examples["input_text"]]
        
    model_inputs = tokenizer(inputs, padding="max_length", truncation=True, max_length=32)
    labels = tokenizer(examples["target_text"], padding="max_length", truncation=True, max_length=32)
    
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized_train_dataset = train_dataset.map(preprocess_function, batched=True)
tokenized_eval_dataset = eval_dataset.map(preprocess_function, batched=True)


training_args = TrainingArguments(
    output_dir="./finetuned_model",
    eval_strategy="epoch",
    save_strategy="epoch",
    save_total_limit=1,
    num_train_epochs=20,
    learning_rate=1e-4,
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    greater_is_better=False,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train_dataset,
    eval_dataset=tokenized_eval_dataset,
    callbacks=[EarlyStoppingCallback(early_stopping_patience=2)],
)

trainer.train()

model.save_pretrained("./finetuned_model")
tokenizer.save_pretrained("./finetuned_model")