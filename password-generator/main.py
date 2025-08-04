import random


alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


# 1. Make list of all the character that use in passeword
# 2. Ask user for how many alphabet, symbols and numbers he/she wants in their password
# 3. Generate a password based on user input 

print("Welcome to the Password Generator")
alphabet_count = int(input("How many numbers alphabets you want in your password: \n"))
symbol_count = int(input("How many numbers alphabets you want in your password: \n"))
number_count = int(input("How many numbers alphabets you want in your password: \n"))


password_chars = []
password_chars += random.choices(alphabet, k=alphabet_count)
password_chars += random.choices(symbols, k=symbol_count)
password_chars += random.choices(numbers, k=number_count)

random.shuffle(password_chars)

password = "".join(password_chars)

print(f"Your generated password is: {password}")