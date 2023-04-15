# Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


# Просим юзера ввести кол-во элементов в списке
n = int(input("Enter the number of elements in the list: "))

# Создаём список длинной n и заполняем его элементами с консоли
A = []
for i in range(n):
    A.append(int(input()))

# Просим юзера ввести число для сравнения
x = int(input("Enter the number to compare against: "))

# Инициализируем переменные для хранения ближайшего элемента и его отличия от X
closest = A[0]
closest_diff = abs(A[0] - x)

# Перебираем список A и находим ближайший элемент к X
for i in range(n):
    diff = abs(A[i] - x)
    if diff < closest_diff:
        closest = A[i]
        closest_diff = diff

# Печатаем результат в консоль
print("The element closest in size to", x, "is", closest, "with a difference of", closest_diff)
