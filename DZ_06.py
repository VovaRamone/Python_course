# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# Просим юзера ввести 6-значное число
ticket_number = input("Enter a six-digit ticket number: ")

# Проверка на валидность внесенных данных
if not ticket_number.isdigit() or len(ticket_number) != 6:
    print("Invalid input. Please enter a six-digit number.")
else:
    # Конвертируем строку в массив цифр
    digits = list(map(int, ticket_number))

    # Складываем циферки
    first_half = digits[0] + digits[1] + digits[2]
    second_half = digits[3] + digits[4] + digits[5]

    # Проверяем нашу удачу
    if first_half == second_half:
        print("Congratulations! You have a lucky ticket!")
    else:
        print("Sorry, this is not a lucky ticket.")




