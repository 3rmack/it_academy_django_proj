# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    incoming = dict(request.POST.items())  # получаем POST запрос и преобразуем в словарь

    vowels = u'аоэиуыеёюя'+'aeiouy'  # шаблон с гласными кирилица + латиница
    consonants = u'бвгджзйклмнпрстфхцчшщ'+'bcdfghjklmnpqrstvwxz'  # шаблон с согласными кирилица + латиница
    count_all = 0  # счетчик всех символов
    count_vowels = 0  # счетчик гласных
    count_consonants = 0  # счетчик согласных
    for item in incoming['Comment']:  # обходим все символы в поле Comment
        count_all += 1  # увеличиваем счетчик всех элементов
        if item in vowels:  # если символ входит в шаблон гласных
            count_vowels += 1  # увеличиваем счетчик гласных
        elif item in consonants:  # если символ входит в шаблон согласных
            count_consonants += 1  # увеличиваем счетчик согласных
    result_string = 'items:{0} vowels:{1} consonants:{2}'.format(count_all, count_vowels, count_consonants)  # формируем строку ответа
    return HttpResponse(result_string)  # ответ
