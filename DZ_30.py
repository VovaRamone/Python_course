# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# get user inputs and generate the list in one line using walrus operator
a1, d, n = int(input("Enter the first element: ")), int(input("Enter the common difference: ")), int(input("Enter the number of elements: "))
progression = [a1 + (i - 1) * d for i in range(1, n+1)]

# print the list
print(*progression, sep='\n')
