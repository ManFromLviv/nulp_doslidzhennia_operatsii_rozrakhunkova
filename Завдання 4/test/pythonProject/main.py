import numpy as np


def multiply_number_by_matrix(number, matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Matrix must be 2x2")

    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            result[i][j] = number * matrix[i][j]

    return result


def add_matrices(matrix1, matrix2):
    if len(matrix1) != 2 or len(matrix1[0]) != 2 or len(matrix2) != 2 or len(matrix2[0]) != 2:
        raise ValueError("Both matrices must be 2x2")

    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result


def inverse_matrix(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2:
        raise ValueError("Matrix must be 2x2")

    # Преобразование в numpy массив
    np_matrix = np.array(matrix)

    # Вычисление определителя
    det = np.linalg.det(np_matrix)
    if det == 0:
        raise ValueError("Matrix is singular, inverse does not exist")

    # Вычисление обратной матрицы
    inverse_np_matrix = np.linalg.inv(np_matrix)

    # Преобразование обратной матрицы обратно в список списков
    inverse_matrix = inverse_np_matrix.tolist()

    return inverse_matrix


def multiply_matrix_by_vector(matrix, vector):
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(vector) != 2:
        raise ValueError("Matrix must be 2x2 and vector must be 1x2")

    result = [0, 0]
    result[0] = matrix[0][0] * vector[0] + matrix[0][1] * vector[1]
    result[1] = matrix[1][0] * vector[0] + matrix[1][1] * vector[1]

    return result

def func(x1, x2):
    return 5 * x1 ** 2 + 2.8 * x1 * x2 + 4.2 * x2 ** 2

def check(x1, x2, eps):
    return (x1 ** 2 + x2 ** 2) ** 0.5 >= eps
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x1 = 7.0
    x2 = 7.2
    eps = 0.1
    lambda_numb = 10 ** 4
    for i in range(1500):
        print(f"Iteration{i+1}")
        start_func = func(x1, x2)
        if not check(x1, x2, eps):
            print("end!")
            print(i+1)
            print(f"\t|grad_F(x^{i})|| = {np.sqrt(x1 ** 2 + x2 ** 2)}>{eps}")
            break
        else:
            print(f"\t|grad_F(x^{i})|| = {np.sqrt(x1 ** 2 + x2 ** 2)}>{eps}")
        print(f"\tstart [x1, x2]: {[x1, x2]}")
        matrix1 = [[1, 0], [1, 0]] # Одинична матриця
        matrix1 = multiply_number_by_matrix(lambda_numb, matrix1)
        matrix2 = [[10, 2.8], [2.8, 8.4]] # Матриця гесе
        matrix3 = add_matrices(matrix1, matrix2)
        matrix4 = inverse_matrix(matrix3)
        matrix5 = [x1, x2]
        matrix6 = multiply_matrix_by_vector(matrix4, matrix5)
        matrix7 = [-matrix6[0], -matrix6[1]]
        x1 += matrix7[0]
        x2 += matrix7[1]
        print(f"\ts^{i}: {matrix7}")
        print(f"\tf(x^{i}) = {start_func}")
        print(f"\tf(x^{i + 1}) = {func(x1, x2)}")
        print(f"\tlambda_numb: {lambda_numb}")
        if func(x1, x2) < start_func:
            lambda_numb *= 0.5
            print(f"\tf(x^{i+1}) < f(x^{i}) => / 2 => {lambda_numb}")
        else:
            lambda_numb *= 2
            print(f"\tf(x^{i+1}) >= f(x^{i}) => * 2 => {lambda_numb}")

        print(f"\tend [x1, x2]: {[x1, x2]}")
        print("===================================================")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
