i = 0
numbers = []


while i < 6:  # setting while condition
    print(f"At the top i is {i}") # prints current value of i
    numbers.append(i) # adds the current value of i to the 'numbers' list

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)