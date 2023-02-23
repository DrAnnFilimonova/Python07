def print_operation_table(operation, rows, columns):
    for x in range(rows):
        row = []
        for y in range(columns):
            row.append(operation(x + 1, y + 1))
        print(row)
print_operation_table(lambda x, y: x*y, 6, 6)