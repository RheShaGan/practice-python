formatter = "{} {} {} {}" #setting a variable called formatter that has 4 blanks

print(formatter.format(1, 2, 3, 4)) #printing the contents of the variable 'formatter' with the blanks replaced by 1,2,3 and 4
print(formatter.format("one", "two", "three", "four")) #printing 'formatter' with the words one two three and four
print(formatter.format(True, False, False, True)) # replacing the blanks in 'formatter' with these boolean values
print(formatter.format(formatter, formatter, formatter, formatter)) #printing 'formatter' where the blanks are replaced with the contents of the 'formatter' variable i.e formatterception
print(formatter.format(
    ".",
    "..",
    "...",
    "...."
)) #prints formatter where the blanks are replaced with the contents in between the quotes