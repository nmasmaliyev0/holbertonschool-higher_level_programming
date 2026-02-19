#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r+") as file:
        lines = file.readlines()

        i = 0
        while i < len(lines):
            if search_string in lines[i]:
                lines.insert(i + 1, new_string)
                i += 2

            i += 1

        file.seek(0)
        file.writelines(lines)
