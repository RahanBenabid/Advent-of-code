import re

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
patternsb = [
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

text = "fiveone 1 twofour"

for pattern in patterns:
    matches = re.findall(pattern, text, re.IGNORECASE)
    for i in matches:
        print("Found in the text: " + i)
