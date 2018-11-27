from sys import argv # how you add features a.k.a modules to your script from the Python feature set
# read the WYSS section for how to run this
name = input("What is your name? ") # prompting the user for additional variables
age = input("How old are you? ")
gender = input("What is your gender? ")
script, first, second, third = argv # unpacking the 'argv' variable

print("The script is called:", script)
print(f"The first variable is {first} and your name is {name}") # printing the argv variables and the user input
print(f"The second variable is {second} and I am {age} years old.")
print(f"The third variable is {third} and I identify with the gender {gender}.")