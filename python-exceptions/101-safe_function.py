#!/usr/bin/python3
import sys


def division(a, b):
    return a / b


def safe_function(fct, *args):
    try:
        return fct(*args)

    except (TypeError, ValueError,  IndexError, ZeroDivisionError) as err:
        print("Exception:", err, file=sys.stderr)
        return None
