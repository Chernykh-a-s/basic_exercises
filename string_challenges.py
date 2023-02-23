# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowel_letters = 'а, е, ё, и, о, у, ы, э, ю, я'
count_vowel_letters = 0
for letters in word.lower():
    if letters in vowel_letters:
        count_vowel_letters += 1
print(f'Количество гласных букв в слове {word}: {count_vowel_letters}')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
word_count = sentence.count(' ') + 1
print(f'Количество слов в предложении: {word_count}')

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
list_sentence = sentence.split()
for letter in list_sentence:
    print(letter[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
len_word = 0
for word in sentence.split():
    len_word += len(word)
avg_len_word = len_word / len(sentence.split())
print(avg_len_word)



























































