# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть


# Просим юзера ввести кол-во монет и их текущее состояние
n = int(input("Enter the number of coins: "))
coins = input("Enter the state of the coins (H for heads, T for tails): ")

# Считаем кол-во монет решкой и гербом
num_heads = coins.count('H')
num_tails = n - num_heads

# Определяем, какой стороной перевернуть, чтобы все монеты оказались одной стороной вверх
num_flips = min(num_heads, num_tails)

# Выводим минимальное количество подбрасываний, необходимое для получения всех монет одной стороной вверх
print("Minimum number of flips needed:", num_flips)

# Переворачиваем монеты, чтобы они оказались одной стороной вверх
if num_flips == num_heads:
    final_state = coins.replace('T', 'H')
else:
    final_state = coins.replace('H', 'T')

# Печатаем результат
print("Final state of coins:", final_state)

