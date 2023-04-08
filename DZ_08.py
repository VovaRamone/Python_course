# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

# Просим юзера ввести данные
n = int(input("Enter the length of the chocolate bar: "))
m = int(input("Enter the width of the chocolate bar: "))
k = int(input("Enter the number of slices you want to break off: "))

# Выполняем проверки. Для успешного результата нам нужно чтобы кол-во отломленных долек делилось без остатка на m или n
if k > n * m:
    print("It is not possible to break off that many slices.")
elif k % n == 0 or k % m == 0:
    print("Yes, it is possible to break off", k, "slices.")
else:
    print("No, it is not possible to break off", k, "slices.")





