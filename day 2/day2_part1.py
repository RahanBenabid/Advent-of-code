import re

final_value = 0



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
    global final_value

    extract_id = re.compile(r"Game (\d*):")
    blue_balls = re.compile(r"(\d*) blue")
    red_balls = re.compile(r"(\d*) red")
    green_balls = re.compile(r"(\d*) green")

    m = extract_id.findall(line)
    b = blue_balls.findall(line)
    g = green_balls.findall(line)
    r = red_balls.findall(line)
    blue_table = [int(x) for x in b]
    green_table = [int(x) for x in g]
    red_table = [int(x) for x in r]

    # print("game :", m[0], " max blue: ", max(blue_table), " max green: ", max(green_table), " max red: ", max(red_table))


    if (int(max(blue_table)) <= loaded_blue) and (int(max(red_table)) <= loaded_red) and (int(max(green_table)) <= loaded_green):
        game_id = int(m[0])
        final_value += game_id
        print(f"Game {game_id} is possible.")

    


if __name__ == "__main__":
    process_phrase(input_text)
    print(final_value)


# 12 red cubes, 13 green cubes, and 14 blue cubes