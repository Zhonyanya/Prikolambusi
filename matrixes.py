def matrix_sum(matrix1, matrix2):
    can_sum = True
    number_of_lines = len(matrix1)
    if number_of_lines == len(matrix2):
        for column in range(number_of_lines):
            if len(matrix1[column]) != len(matrix2[column]):
                can_sum = False
                break
    if can_sum:
        new_matrix = [[0] *  len(matrix1[0])] * number_of_lines
        for line in range(number_of_lines):
            for column in range(len(matrix1[0])):
                new_matrix[line][column] = matrix1[line][column] + matrix2[line][column]
        return new_matrix
    else:
        return "Ашипка"
