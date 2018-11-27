from sys import argv # import argv module

##script, filename = argv # assign scriptname and filename as values to be unpacked by the argv variable

##txt = open(filename) # assigning filename to be opened to txt variable

##print(f"Here's your file {filename}:") #print statement
##print(txt.read()) # apply read function on variable that stores txt file

print("Type the filename again:")
file_again = input("> ") #get user input

txt_again = open(file_again) #store txt from file in variable

print(txt_again.read()) #read text contents 