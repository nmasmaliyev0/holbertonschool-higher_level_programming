#!/usr/bin/python3
from sys import argv


def main():
    if len(argv) - 1 == 0:
        print("{} arguments.".format(0))
        return
    elif len(argv) - 1 == 1:
        print("{} argument:".format(1))
    else:
        print("{} arguments:".format(len(argv) - 1))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
