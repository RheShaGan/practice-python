from sys import argv #import module

script, filename = argv # assign variables to argv

your_file = open(filename)
print("So your file now looks like: ", your_file.read())

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w') # opening the file and truncating it

print("Truncating the file. Goodbye!")
target.truncate() # empties the file

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# writing the inputs from the user for each line to the file
target.write(line1 +"\n" + line2 + "\n" + line3 + "\n" )
## target.write("\n")
## target.write(line2)
## target.write("\n")
## target.write(line3)
## target.write("\n")

## print("Your newly edited file now looks like this: ")
## target.read()

print("And finally, we close it.")
target.close() # closing the file


