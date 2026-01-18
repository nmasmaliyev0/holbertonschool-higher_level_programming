#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_of_a_times_b = 0
    sum_of_b = 0

    for a, b in my_list:
        sum_of_a_times_b += a * b
        sum_of_b += b

    return sum_of_a_times_b / sum_of_b
