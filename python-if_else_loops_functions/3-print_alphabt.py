#!/usr/bin/python3
for id in range(97, 123):
    if id == 101 or id == 113:
        continue
    print("{}".format(chr(id)), end="")
