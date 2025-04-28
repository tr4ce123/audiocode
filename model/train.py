from transformers import T5ForConditionalGeneration, T5Tokenizer, Trainer, TrainingArguments, EarlyStoppingCallback, RobertaTokenizer
from datasets import Dataset
import pandas as pd

df = pd.read_csv("./model/training_data_fixed.csv", quotechar='"')

dataset = Dataset.from_pandas(df)
dataset = dataset.train_test_split(test_size=0.1, seed=42)
train_dataset = dataset["train"]
eval_dataset = dataset["test"]

print(train_dataset)
print(eval_dataset)

# tokenizer = T5Tokenizer.from_pretrained("salesforce/codet5-small")
tokenizer = RobertaTokenizer.from_pretrained("Salesforce/codet5-small")

model = T5ForConditionalGeneration.from_pretrained("Salesforce/codet5-small")

def preprocess_function(examples):
    inputs = ["translate instruction to code: " + instr for instr in examples["input_text"]]
        
    model_inputs = tokenizer(inputs, padding="max_length", truncation=True, max_length=256)
    labels = tokenizer(examples["target_text"], padding="max_length", truncation=True, max_length=256)
    
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized_train_dataset = train_dataset.map(preprocess_function, batched=True)
tokenized_eval_dataset = eval_dataset.map(preprocess_function, batched=True)


training_args = TrainingArguments(
    output_dir="./finetuned_model",
    eval_strategy="epoch",
    save_strategy="epoch",

    # all of these lines essentially mean that we keep the model with the lowest loss
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    greater_is_better=False,
    save_total_limit=1,

    # keep epochs at a reasonable number like 10. any more could be overkill as the loss curve will start going up (we're overfitting)
    num_train_epochs=8,

    # this is a "medium-slower rate". steady convergence, but not too slow
    learning_rate=5e-5,
    
    # after every gradient step, shrink the weight back towards 0
    # why: helps to generalize the model by preventing overfitting because the dataset is small. don't want the model to be "too strong"
    weight_decay=0.01,

    # start learning rate small, then gradually increase it over the first 50 steps of the gradient
    # don't want chaotic training early
    warmup_steps=50,
    
    # learning rate scheduler makes the learning rate start high, the slow down as training finishes
    # this is one of the most popular scheduler types and adds "polish"
    lr_scheduler_type="cosine",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_train_dataset,
    eval_dataset=tokenized_eval_dataset,

    # stop early if the loss increases two times in a row, we're overfitting
    callbacks=[EarlyStoppingCallback(early_stopping_patience=2)],
)

trainer.train()

model.save_pretrained("./finetuned_model")
tokenizer.save_pretrained("./finetuned_model")