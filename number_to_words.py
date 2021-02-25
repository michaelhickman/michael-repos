"""number_to_word.py."""

import re

UNIT = (
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen"
)

TENS = (
    "",
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
)

THOUSANDS = (
    "",
    "thousand",
    "million",
    "billion",
    "trillion"
)


def parse_file(path):
    """Parse the input .txt file."""
    try:
        with open(path, 'r') as f:
            sentences = [line for line in f]  # extract lines
    except:
        return []  # return empty list if fail to open file
    return sentences


def valid_number(sentence):
    """Validate input sentence."""
    string = re.sub(r"(?<=\d)[^A-Za-z0-9]+(?=\d)", ' ', sentence)
    matches = re.findall(r"(?<=\s)\d+(?=\s)|(?<=\s)\d+$", string)
    if not matches or len(matches) > 1:
        return False, 'number invalid'
    number = matches.pop()
    if len(number) > len(THOUSANDS) * 3:
        return False, 'number invalid'
    return True, number


def get_words(n):
    """Convert a three digit string number in to words."""
    a, b, c, d = n[0], n[1], n[2], n[-2:]

    output = ""

    if int(d) < 20:
        output = UNIT[int(d)]
    elif int(d) % 10 == 0:
         output = TENS[int(b)]
    else:
        output = TENS[int(b)] + "-" + UNIT[int(c)]

    if a != "0" and d != "00":
        output = UNIT[int(a)] + " hundred and " + output
    elif a != "0" and d == "00":
        output = UNIT[int(a)] + " hundred"

    return output


def convert(str_number):
    """Convert a string number into words."""
    words = ""

    if int(str_number) == 0:
        return "zero"

    while len(str_number) % 3 != 0:
        str_number = "0" + str_number

    split_list = [
        str_number[i - 3:i]
        for i in range(len(str_number), 0, -3)
    ]

    split_list = [
        (idx, val)
        for idx, val in enumerate(split_list)
        if val != "000"
    ]

    for index, obj in enumerate(split_list):
        old_index, number = obj
        if index == 0 and old_index == 0:
            words = get_words(number)
        elif index == 0 and old_index != 0:
            words = f"{get_words(number)} {THOUSANDS[old_index]}"
        elif index == 1 and str_number[-3] == "0":
            words = f"{get_words(number)} {THOUSANDS[old_index]} and {words}"
        elif index == 1 and str_number[-3] != "0" and str_number[-2:] == "00":
            words = f"{get_words(number)} {THOUSANDS[old_index]} and {words}"
        else:
            words = f"{get_words(number)} {THOUSANDS[old_index]}, {words}"

    return words


sentences = parse_file(r'C:\Users\micha\OneDrive\Desktop\91\test_cases.txt')

for sentence in sentences:
    flag, msg = valid_number(sentence)
    if flag:
        print(convert(msg))
        continue
    print(msg)