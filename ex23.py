import sys
script, encoding, error = sys.argv #command-line argument handling code

def main(language_file, encoding, errors): #function to read a single line of text file
    line = language_file.readline() # readline function returns empty string

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) # looping the function main within itself based on results of if-statement

def print_line(line, encoding, errors): # function to encode each line from text file
    next_lang = line.strip() # simple strippin of trailing \n on the line string
    raw_bytes = next_lang.encode(encoding, errors=errors) # encoding strings to bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors) # decoding bytes to strings again

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)  