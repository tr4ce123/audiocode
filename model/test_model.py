from transformers import T5ForConditionalGeneration, T5Tokenizer, RobertaTokenizer

model = T5ForConditionalGeneration.from_pretrained("./finetuned_model")
# tokenizer = T5Tokenizer.from_pretrained("./finetuned_model")
tokenizer = RobertaTokenizer.from_pretrained("./finetuned_model")


def generate_code(prompt: str) -> str:
    text = "translate instruction to code: " + prompt.strip()
    enc  = tokenizer(text, return_tensors="pt")
    out  = model.generate(
        **enc,
        max_new_tokens=64,
        num_beams=4,
        early_stopping=True,
    )
    return tokenizer.decode(out[0], skip_special_tokens=True)
# examples = [
#     "Create a list called nums",
#     "Initialize a deque with 2",
#     "Create an empty dictionary called config",
#     "Make an empty string called hello",
#     "Sort a list called nums in ascending order",
#     "initialize an empty set called jewels",
#     "initialize a default dictionary with zero default value",
#     "Write a function called add_numbers that takes in a parameter x and a parameter y. Inside the function, make a new variable called z that is equal to x plus y. Return z",
#     "Write an if-else block that checks if the variable is_authenticated is true. If it is, return the string logged in. If not, return the string not logged in",
#     "Create an empty list called tasks and append the string study",
#     "Create a Counter object from a list called words",
#     "Write a function named greet that takes a name and returns the string hello, name!",
#     "write a for loop that starts at 0 and goes to n"
# ]

examples = [
    "Create a list called groceries",
    "Create an empty dictionary called user_info",
    "Make an empty set called inventory",
    "Initialize a Counter object from a list called votes",
    "Create a deque with elements 1 and 2",
    "Initialize a default dictionary with float as default value",
    "Create a string called message and set it to welcome",
    "Make a list called squares containing numbers 1 through 5 squared",
    "Create a tuple named coordinates with two values",
    "Create a boolean variable called is_online and set it to true",
    "Write a function called multiply that takes parameters a and b and returns their product",
    "Write a function called greet_user that takes a name and prints hello followed by the name",
    "Write a function called add_five that accepts an integer x and returns x plus five",
    "Write a function called is_even that checks if a number is even and returns true or false",
    "Write an if-else block that checks if a variable score is greater than 70. if it is, print pass. if not, print fail",
    "Write an if-else block that checks if a list called items is empty. if it is, print empty. if not, print the string not empty",
    "Write a for loop that iterates from 0 to 4 and prints each number",
    "Write a for loop that goes through a list called cities and prints each city in uppercase",
    "Write a for loop that adds all numbers from 1 to 10 into a variable called total",
    "Write a for each loop that checks each word in words. if the word length is greater than 5, print long word",
    "Create a while loop that runs while x is less than 10. inside the loop, add 1 to x",
    "Write a while loop that continues as long as the list queue is not empty. inside the loop, pop an element",
    "Create a for loop that prints odd numbers from 1 to 9",
    "Write an if-elif-else block that checks if variable n is zero, positive, or negative and prints the result",
    "Create a list comprehension that creates a list of even numbers between 0 and 10",
]

for example in examples:
    code = generate_code(example)
    print(f"Input: {example}\nGenerated Code: {code}\n{'-'*50}")