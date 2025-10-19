def matrix_sum(matrix1, matrix2):
    can_sum = True
    number_of_lines = len(matrix1)
    number_of_columns = len(matrix1[0])
    if number_of_lines == len(matrix2):
        for line in range(number_of_lines):
            if len(matrix1[line]) != len(matrix2[line]):
                can_sum = False
                break
    if can_sum:
        new_matrix = [[0 for _ in range(number_of_columns)] for _ in range(number_of_lines)]
        print(new_matrix)
        for line in range(number_of_lines):
            for column in range(number_of_columns):
                new_matrix[line][column] = matrix1[line][column] + matrix2[line][column]
        return new_matrix
    else:
        return "Ашипка"
