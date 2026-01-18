#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    
    max_value = max(a_dictionary.values())
    key = [k for k, v in a_dictionary.items() if v == max_value]

    return key
