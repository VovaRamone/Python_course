# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.


def check_rhythm(poem):
    phrases = poem.split(" ")
    syllables = set()
    
    for phrase in phrases:
        words = phrase.split("-")
        phrase_syllables = sum(word.count(vowel) for word in words for vowel in "aeiouAEIOU")
        syllables.add(phrase_syllables)
    
    if len(syllables) == 1:
        return "Param pam-pam"
    else:
        return "Pam param"

poem = input("Enter Winnie the Pooh's poem: ")
result = check_rhythm(poem)
print(result)

