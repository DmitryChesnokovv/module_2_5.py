def get_matrix(n, m, value):
    if n <= 0 or m <= 0:
        return
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)

    return matrix


result1 = get_matrix(3, 2, [11, 12, 13])
result2 = get_matrix(4, 3, [14, 15])
result3 = get_matrix(2, 4, [17, 18])
result4 = get_matrix(1, 5, [20, 21, 22, 24])


print(result1)
print(result2)
print(result3)
print(result4)
