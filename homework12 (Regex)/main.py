from typing import List
import re

'''
Выведите все подстроки, содержащие "cat".
'''

string = 'human aaaa bbbb cccc sdfjbksdcat gkdgcatdg cat catcat dskbfjhsd z111z  18-02-2024 z22z zzzzz Atbbes utes if else for 4 -5 4.2 4.3 -6.7 human 18-03-2024'


def find_cat_substrings(string: str) -> None:
    substrings = re.findall(r'\b\w*cat\w*\b', string)
    print('find cat substrings: ', substrings)


'''
Выведите строки, содержащие две буквы "z", между которыми ровно три символа.
'''


def find_zz_substrings(string: str) -> None:
    zz_substrings = re.findall(r'z[^ ]{3}z', string)
    print('find zz substrings: ', zz_substrings)


'''
Номер должен быть длиной 10 знаков и начинаться с 8 или 9. Есть список телефонных номеров, и нужно проверить их, используя регулярные выражения в Python
'''


def check_phone_numbers(phone_numbers: List[str]):
    pattern = r'^[89]\d{9}$'

    for number in phone_numbers:
        if re.match(pattern, number):
            print('valid number: ', number)
        else:
            print('invalid number: ', number)


phone_numbers = ['89234567890', '79994537766',
                 '1234567890', '9876543210', '1876543210', '8823456789']

''''
Дана строка, выведите все вхождения слов, начинающиеся на гласную букву.
'''


def find_vowel_substrings(string: str) -> None:
    pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'
    vowel_substrings = re.findall(pattern, string)
    print('find vowel substrings: ', vowel_substrings)


'''
Дана строка. Вывести все числа этой строки, как отрицательные так и положительные. 
'''


def find_numbers(string: str) -> None:
    pattern = r'-?\d+\.?\d*'
    numbers = re.findall(pattern, string)
    print('find numbers: ', numbers)


''''
В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.
'''


def replace_word(string: str) -> None:
    string.replace('human', 'computer')
    print('replace word: ', string)


'''
Извлечь дату из строки. Формат даты dd –mm-yyyy (например, 2022-02-28).
'''


def find_date(string: str) -> None:
    pattern = r'\b\d{2}-\d{2}-\d{4}\b'
    dates = re.findall(pattern, string)
    print('find date: ', dates)


'''
Найти все слова, в которых есть хотя бы одна буква ‘b’
'''


def find_b_substrings(string: str) -> None:
    pattern = r'\b\w*b\w*\b'
    words = re.findall(pattern, string)
    print('find b substrings: ', words)


'''
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву. Буквой считается символ из группы \w.
'''


def replace_repeated_letters(string: str) -> None:
    pattern = r'(\w)\1+'
    replaced_text = re.sub(pattern, r'\1', string)
    print('replace repeated letters: ', replaced_text)


''''
Поиск URL. Это регулярное выражение находит URL-адреса, начинающиеся с "http://" или "https://", 
далее допускается "www." (опционально), за которым следует доменное имя, а затем дополнительный путь и параметры.
'''

text = 'https://proglib.io/p/python-oop or http://proglib.io/p/python-oop or https://www.proglib.io/p/python-oop or htps://proglib.io/p/python-oop'


def find_urls(text: str) -> None:
    pattern = r'https?://(?:www\.)?\w+\.\w+(?:/\S*)?'
    urls = re.findall(pattern, text)
    print('find urls: ', urls)


'''
Напишите регулярное выражение для поиска всех HTML тегов в тексте
'''

text2 = "<div class='wrapper'><p>Hello, <strong>дивный новый мир</strong>!</p></div>"


def find_html_tags(text: str) -> None:
    pattern = r'<[^>]+>'
    html_tags = re.findall(pattern, text)
    print('html tags: ', html_tags)


find_cat_substrings(string)
find_zz_substrings(string)
check_phone_numbers(phone_numbers)
find_vowel_substrings(string)
find_numbers(string)
replace_word(string)
find_date(string)
find_b_substrings(string)
replace_repeated_letters(string)
find_urls(text)
find_html_tags(text2)
