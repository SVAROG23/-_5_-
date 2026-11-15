import matplotlib.pyplot as plt
import numpy as np


def get_user_input():
    "Функция для ввода данных."
    print("Ввод данных")
    print("По умолчанию: от -3 до 3 с шагом 0.5.")
    print("Нажмите Enter, чтобы использовать значения по умолчанию.")

    # Вводим значения как строки
    min_str = input("Введите минимальное значение X: ")
    max_str = input("Введите максимальное значение X: ")
    step_str = input("Введите шаг: ")

    # Если пользователь ничего не ввел, ставим значения по умолчанию
    if min_str == "":
        x_min = -3.0
    else:
        x_min = float(min_str)

    if max_str == "":
        x_max = 3.0
    else:
        x_max = float(max_str)

    if step_str == "":
        step = 0.5
    else:
        step = float(step_str)

    # Проверка
    if step <= 0:
        print("Ошибка: шаг должен быть больше нуля. Ставлю 0.5.")
        step = 0.5

    if x_min >= x_max:
        print("Ошибка: минимум больше максимума. Ставлю от -3 до 3.")
        x_min = -3.0
        x_max = 3.0

    return x_min, x_max, step


def plot_functions(x_min, x_max, step):
    "Функция для построения графиков."
    # Создаем массив X с помощью numpy
    x = np.arange(x_min, x_max + step / 2, step)

    # Считаем Y
    y_square = x ** 2
    y_cube = x ** 3

    # Размер фигуры (по заданию)
    plt.figure(figsize=(8, 5))

    # График x^2 (синий, пунктир, кружочки)
    plt.plot(
        x, y_square, color='blue', linestyle='--', marker='o', label='y = x^2'
    )

    # График x^3 (красный, сплошной, квадратики)
    plt.plot(
        x, y_cube, color='red', linestyle='-', marker='s', label='y = x^3'
    )

    # Подписи (по заданию)
    plt.title('Графики функций y = x^2 и y = x^3')
    plt.xlabel('Значения X')
    plt.ylabel('Значения Y')
    plt.grid(True)
    plt.legend(loc='upper left')

    plt.show()


if __name__ == "__main__":
    # Получаем данные
    a, b, h = get_user_input()

    # Строим график
    plot_functions(a, b, h)
