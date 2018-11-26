print("how old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input() #input() only accepts strings as args
# putting an 'end=' '' at the end of each print line tells print not to end the line with a newline character and go to the next line.
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
