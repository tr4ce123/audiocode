from transformers import T5ForConditionalGeneration, T5Tokenizer

model = T5ForConditionalGeneration.from_pretrained("./finetuned_model")
tokenizer = T5Tokenizer.from_pretrained("./finetuned_model")

def generate_code(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=128)
    outputs = model.generate(**inputs, max_new_tokens=64)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

examples = [
    "Create a list called nums",
    "Initialize a deque with 2",
    "Create an empty dictionary called config",
    "Make an empty string called hello",
    "Sort a list of numbers in descending order",
    "initialize an empty set called jewels",
    "initialize a default dictionary with zero default value"
]

for example in examples:
    code = generate_code(example)
    print(f"Input: {example}\nGenerated Code: {code}\n{'-'*50}")