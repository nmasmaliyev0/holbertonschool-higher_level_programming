#!/usr/bin/python3
def pascal_triangle(n):
    triangle = []

    for i in range(n):
        row = [1]

        if i == 0:
            triangle.append(row)
            continue

        prev = triangle[i - 1]
        for j in range(len(prev) - 1):
            value = prev[j] + prev[j + 1]
            row.append(value)

        row.append(1)
        triangle.append(row)

    return triangle
