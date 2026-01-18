#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0

    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    romans_special = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    i = 0
    number = 0

    while i < len(roman_string):
        if roman_string[i: i + 2] in romans_special:
            number += romans_special[roman_string[i: i + 2]]
            i += 2
        else:
            number += romans[roman_string[i]]
            i += 1

    return number
