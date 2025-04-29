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
    "Create an empty list called results",
    "Make a dictionary called person with keys name and age",
    "Create a set called primes containing 2, 3, and 5",
    "Initialize a deque named history with no elements",
    "Create a Counter object based on a list named votes",
    "Make a default dictionary called scores with int as default value",
    "Create a string variable called greeting and set it to hello world",
    "Create a list called doubled containing numbers from 1 to 5 each multiplied by 2",
    "Make a tuple named position with three coordinates",
    "Initialize a boolean variable is_active and set it to false",
    "Write a function called divide that takes parameters x and y and returns x divided by y",
    "Write a function named print_welcome that accepts a name and prints welcome plus the name",
    "Write a function called subtract_ten that takes a number and returns it minus 10",
    "Write a function called is_positive that checks if a number is greater than zero and returns true or false",
    "Write an if-else block that checks if temperature is above 30. If it is, print hot. Otherwise, print cold",
    "Write an if-else block that checks if the list tasks is empty. If it is, print no tasks. Otherwise, print tasks available",
    "Write a for loop that prints numbers from 5 to 10",
    "Write a for loop that goes through a list called colors and prints each color reversed",
    "Create a for loop that adds all numbers from 10 to 1 into a variable called sum",
    "Write a for each loop that checks each item in cart. If the item is expensive, print expensive item",
    "Create a while loop that runs while counter is less than 5. Inside the loop, increase counter by 2",
    "Write a while loop that pops elements from stack until it is empty",
    "Create a for loop that prints even numbers from 2 to 10",
    "Write an if-elif-else block that checks if a number n is less than 0, equal to 0, or greater than 0 and prints a message",
    "Create a list comprehension that builds a list of squares of numbers from 0 to 4",
    "Write a function named dfs that takes in a parameter start_node.",
    "create a blank line"
]

for example in examples:
    code = generate_code(example)
    print(f"Input: {example}\nGenerated Code: {code}\n{'-'*50}")