#include <iostream>
#include <fstream>
#include <string>

bool is_num(char c) {
    return ('0' <= c && c <= '9');
}

bool parse_one(std::string input_string, int pos) {
    bool is_one = false;

    if (pos+1 < input_string.length()) {
        is_one = (input_string[pos] == 'n' && input_string[pos+1] == 'e');
    }

    return is_one;
}

bool parse_two(std::string input_string, int pos) {
    bool is_two = false;

    if (pos+1 < input_string.length()) {
        is_two = (input_string[pos] == 'w' && input_string[pos+1] == 'o');
    }

    return is_two;
}

bool parse_three(std::string input_string, int pos) {
    bool is_three = false;

    if (pos+3 < input_string.length()) {
        is_three = (input_string[pos] == 'h' && input_string[pos+1] == 'r' && input_string[pos+2] == 'e' && input_string[pos+3] == 'e');
    }

    return is_three;
}

bool parse_four(std::string input_string, int pos) {
    bool is_four = false;

    if (pos+2 < input_string.length()) {
        is_four = (input_string[pos] == 'o' && input_string[pos+1] == 'u' && input_string[pos+2] == 'r');
    }

    return is_four;
}

bool parse_five(std::string input_string, int pos) {
    bool is_five = false;

    if (pos+2 < input_string.length()) {
        is_five = (input_string[pos] == 'i' && input_string[pos+1] == 'v' && input_string[pos+2] == 'e');
    }

    return is_five;
}

bool parse_six(std::string input_string, int pos) {
    bool is_six = false;

    if (pos+1 < input_string.length()) {
        is_six = (input_string[pos] == 'i' && input_string[pos+1] == 'x');
    }

    return is_six;
}

bool parse_seven(std::string input_string, int pos) {
    bool is_seven = false;

    if (pos+3 < input_string.length()) {
        is_seven = (input_string[pos] == 'e' && input_string[pos+1] == 'v' && input_string[pos+2] == 'e' && input_string[pos+3] == 'n');
    }

    return is_seven;
}

bool parse_eight(std::string input_string, int pos) {
    bool is_eight = false;

    if (pos+3 < input_string.length()) {
        is_eight = (input_string[pos] == 'i' && input_string[pos+1] == 'g' && input_string[pos+2] == 'h' && input_string[pos+3] == 't');
    }

    return is_eight;
}

bool parse_nine(std::string input_string, int pos) {
    bool is_nine = false;

    if (pos+2 < input_string.length()) {
        is_nine = (input_string[pos] == 'i' && input_string[pos+1] == 'n' && input_string[pos+2] == 'e');
    }

    return is_nine;
}

bool parse_zero(std::string input_string, int pos) {
    bool is_zero = false;

    if (pos+2 < input_string.length()) {
        is_zero = (input_string[pos] == 'e' && input_string[pos+1] == 'r' && input_string[pos+2] == 'o');
    }

    return is_zero;
}

int parse_string_from_pos(std::string input_string, int pos) {
    int val = -1;

    int i=pos;
    if (input_string[i] == 'o') {
        if (parse_one(input_string, pos+1)) {
            val = 1;
        }
    }
    else if (input_string[i] == 't') {
        if (parse_two(input_string, pos+1)) {
            val = 2;
        }
        else if (parse_three(input_string, pos+1)) {
            val = 3;
        }
    }
    else if (input_string[i] == 'f') {
        if (parse_four(input_string, pos+1)) {
            val = 4;
        }
        else if (parse_five(input_string, pos+1)) {
            val = 5;
        }
    }
    else if (input_string[i] == 's') {
        if (parse_six(input_string, pos+1)) {
            val = 6;
        }
        else if (parse_seven(input_string, pos+1)) {
            val = 7;
        }
    }
    else if (input_string[i] == 'e') {
        if (parse_eight(input_string, pos+1)) {
            val = 8;
        }
    }
    else if (input_string[i] == 'n') {
        if (parse_nine(input_string, pos+1)) {
            val = 9;
        }
    }
    else if (input_string[i] == 'z') {
        if (parse_zero(input_string, pos+1)) {
            val = 0;
        }
    }
    return val;
}

void get_first_and_last_numbers(std::string input_string, int &first_number, int &last_number) {
    int i=0;

    // get the first number
    while (i < input_string.length() && first_number == -1) {
        if (is_num(input_string[i])) {
            first_number = input_string[i] - '0';
        }
        else {
            first_number = parse_string_from_pos(input_string, i);
        }
        i++;
    }

    // get the last number
    while (i < input_string.length()) {
        int temp_last_val = parse_string_from_pos(input_string, i);

        if (is_num(input_string[i])) {
            temp_last_val = input_string[i] - '0';
        }
        else {
            temp_last_val = parse_string_from_pos(input_string, i);
        }

        if (temp_last_val > 0) {
            last_number = temp_last_val;
        }
        i++;
    }
}



int main(int argc, char **argv) {
    std::ifstream myfile;
    myfile.open("lect.txt");

    std::string mystring;

    int final_val = 0;

    while (std::getline(myfile, mystring)) {
        int first_val = -1;
        int last_val = -1;

        get_first_and_last_numbers(mystring, first_val, last_val);

        if (last_val == -1) {
            last_val = first_val;
        }

        final_val += first_val*10 + last_val;
    }

    std::cout << "Final added value is " << final_val << '\n';
}