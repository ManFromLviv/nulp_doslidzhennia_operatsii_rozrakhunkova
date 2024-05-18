import numpy as np


# Функція, яку ми хочемо мінімізувати
def func(x, y):
    return x ** 2 + 4 * x * y + 2 * y ** 2 - 6 * x - 8 * y


# Початкова точка
x, y = 0, 0

# Параметри методу Хука-Дживса
step_size = 1
reduction_factor = 0.5
tolerance = 1e-6
max_iterations = 1000

# Початкова оцінка для кроку
delta_x, delta_y = step_size, step_size

# Цикл оптимізації
for _ in range(max_iterations):
    # Знаходимо значення функції в поточій точці
    current_value = func(x, y)

    # Шукаємо нову точку в напрямку найменшого спуску
    next_x = x - delta_x
    next_y = y - delta_y
    next_value = func(next_x, next_y)

    # Перевіряємо, чи зменшилась значення функції
    if next_value < current_value:
        x, y = next_x, next_y
    else:
        # Зменшуємо крок
        delta_x *= reduction_factor
        delta_y *= reduction_factor

    # Перевіряємо критерій зупинки
    if max(abs(delta_x), abs(delta_y)) < tolerance:
        break

print("Мінімум функції знайдено в точці:", (x, y))
print("Значення функції в мінімумі:", func(x, y))
