import re 
r=re.compile("[.]*\d[.]*")
table = []
n=0
input_string =""

def processline(line):

    m=r.findall(line)
    k = int(m[0] + m[-1])
    table.append(k)


def process_phrase(phrase):

    # Split the phrase into lines using '\n'
    lines = phrase.split('\n')

    # Process each line using the processline function
    for line in lines:
        processline(line)


if __name__ == "__main__":

    # Example phrase with newline characters
    with open('lect.txt', 'r') as file:
        input_string = file.read()

    # Call the function to process the entire phrase
    process_phrase(input_string)

    print(table)
    for i in table:
        n += i
    print("total shitty shit: " + str(n))