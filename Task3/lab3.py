import re
# вариант 1

test1 = '''Классное слово – обороноспособность, которое должно идти после слов: трава и молоко.'''
test2 = '''Пусто, решений нет.'''
test3 = '''Добро молоко город молот голод щавель топот топ.'''
test4 = '''Абонемент и олово шли за городом.'''
test5 = '''Носок купил себе башмак и попал в просак. Затем купил себе молоток и забил гвоздь в комод.'''

def find_words(filename):

    words = re.split(r'(\s)', filename)                  # разбивка слов по элементам
    res = []                                             # создание спика для хранения финального результата
    for word in words:                                      # цикл для элементов в разбивке
        if chek_word(word):                                  # проверка слова

            res.append(re.sub(r'[.,:?!]$', '', word))   # добавляю в массив слова, при этом знаки препинания удаляются
    res.sort(key = len)                                 # сортировка результата по увеличению длины слова


    for word in res:
        print(word)

def chek_word(word):
    chars = re.findall(r'[аоеёиыуэюя]', word, re.IGNORECASE)
    if len(chars) == 0:
        return False
    result = True
    for char in chars:
        if not re.match(chars[0], char, re.IGNORECASE):
            result = False
    return result


def main():
    print(' Test 1: ')
    find_words(test1)
    print(' Test 2: ')
    find_words(test2)
    print(' Test 3: ')
    find_words(test3)
    print(' Test 4: ')
    find_words(test4)
    print(' Test 5: ')
    find_words(test5)


if __name__ == '__main__':
    main()


   # final = []
    #for i in final_words:
     #   final.append(i[0])
   # return sorted(final, key=len)


#for i in range(1, 6):
 #   string_name = 'test' + str(i) + '.txt'
  #  words_list = find_words(string_name)
