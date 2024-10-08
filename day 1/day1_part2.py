import re
table = []          #table that contains our correct matches Ex: 12 77 38 22 65
matches = []        #matches of the analysis of an entire line
# digits = []         
input_string = ""   #the input string of the site
result = 0          #the result of an analysis of a whole line
final_result = 0

#dictionnaire
word_to_digit = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0
}

pattern = r"\b(?:(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|\d)\b"
def process_phrase(phrase):

    # Split the phrase into lines using '\n'
    lines = phrase.split('\n')

    # Process each line using the processline function
    for line in lines:
        print("hi " + line)
        process_Line(line)

def process_Line(line):
    global matches
    matches = []  
    for match in re.finditer(pattern, line, re.IGNORECASE):
        matches.append(match.group())


    matches.sort(key=lambda x: line.find(x))
    
    if matches:  # Check if matches is not empty
        table.append(int(matches[0] + matches[-1]))


# print(matches)

if __name__ == "__main__":

    with open("lect.txt", "r") as file:
        input_string = file.read()

    process_phrase(input_string)

    for i in table:
        final_result += i

    print(final_result)