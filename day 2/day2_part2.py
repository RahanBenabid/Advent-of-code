import re

power_set = 0

loaded_red = 12
loaded_green = 13
loaded_blue = 14

digits = []

input_text = ""
with open('/Users/RahanBen/Downloads/-Etudes/-Solo/AOC/day 2/input.txt', 'r') as file:
    input_text = file.read()
# print(input_text)

def process_phrase(phrase):

    # Split the phrase into lines using '\n'
    lines = phrase.split('\n')

    # Process each line using the processline function
    for line in lines:
        process_line(line)


def process_line(line):
    global power_set

    extract_id = re.compile(r"Game (\d*):")
    blue_balls = re.compile(r"(\d*) blue")
    red_balls = re.compile(r"(\d*) red")
    green_balls = re.compile(r"(\d*) green")

    b = blue_balls.findall(line)
    g = green_balls.findall(line)
    r = red_balls.findall(line)
    blue_table = [int(x) for x in b]
    green_table = [int(x) for x in g]
    red_table = [int(x) for x in r]

    power_set = power_set + (max(blue_table)*max(green_table)*max(red_table))


if __name__ == "__main__":
    process_phrase(input_text)
    print(power_set)


# 12 red cubes, 13 green cubes, and 14 blue cubes