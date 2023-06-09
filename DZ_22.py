# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


import random
from collections import Counter

n = int(input("Введите количество элементов первого множества (от 1 до 10): "))
m = int(input("Введите количество элементов второго множества (от 1 до 10): "))

if n <= 0 or m <= 0:
    print("Ошибка: количество элементов должно быть положительным числом.")
    exit()

# Генерируем первый набор чисел
set1 = [random.randint(1, 10) for i in range(n)]

# Генерируем второй набор чисел
set2 = [random.randint(1, 10) for i in range(m)]

# Создаем объекты Counter для каждого набора чисел
counter1 = Counter(set1)
counter2 = Counter(set2)

# Находим пересечение множеств
intersection = sorted(list((counter1 & counter2).elements()))

# Выводим результат
print("Первое множество: ", set1)
print("Второе множество: ", set2)
print("Элементы, которые встречаются в обоих наборах: ", end="")
for num in intersection:
    print(num, end=" ")




