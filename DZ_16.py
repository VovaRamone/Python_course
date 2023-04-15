# Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# Просим юзера ввести кол-во элементов в списке
n = int(input("Enter the number of elements in the list: "))

# Создаём список длинной n и заполняем его элементами с консоли
A = []
for i in range(n):
    A.append(int(input()))

# Просим юзера ввести искомое число
x = int(input("Enter the number to search for: "))

# Инициализируем переменную счетчика для подсчета количества вхождений X
count = 0

# Перебираем список A и подсчитываем количество вхождений X
for i in range(n):
    if A[i] == x:
        count += 1

# Выводим результат в консоль
print("The number", x, "occurs", count, "times in the list.")