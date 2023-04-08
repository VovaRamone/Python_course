# Найдите сумму цифр трехзначного числа.

# Просим юзера ввести 3-значное число
num = input("Enter a three-digit number: ")

# Проверка на 3-значность
if len(num) != 3 or not num.isdigit():
    print("Invalid input. Please enter a three-digit number.")
else:
    # Конвертируем в числовую переменную и суммируем цифры
    digit_sum = int(num[0]) + int(num[1]) + int(num[2])
    print("The sum of the digits of", num, "is", digit_sum)




