# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# рекурсивная функция для возведения числа в степень
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

# получаем значения числа и степени от пользователя
our_num = int(input("Введите число: "))
our_degree = int(input("Введите степень: "))

# вызываем функцию power и выводим результат
result = power(our_num, our_degree)
print(f"{our_num} в степени {our_degree} равно {result}")
