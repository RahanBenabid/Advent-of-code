import re
matches = []
digits = []

patterns = [
    r"zero",
    r"one",
    r"two",
    r"three",
    r"four",
    r"five",
    r"six",
    r"seven",
    r"eight",
    r"nine",
    r"[.]*\d[.]*"
    ]

input_string = "Thi lalfive21ala80nnfive1ethree0four9none6eightit."

for pattern in patterns:
    for match in re.finditer(pattern, input_string):
        matches.append(match.group())
matches.sort(key=lambda x: input_string.find(x))



print(matches)


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


for i in matches:
    print(i)
    if i in word_to_digit:
        digits.append(word_to_digit[i])

print(digits)