#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
#
# Created at 12.09.2020.
# Python 3.7.3 x64
# Contacts: alexandrsokolov@cock.li
#
"""
пользователь начинает игру указывая первый город
если города нет в списке, то говорим ему что надо указать город другой
заносим город с список уже названных городов
получаем название города первая буква которого начинается с последней буквы названного
выводим на экран
если городов не осталдось, то пользователь выйграл
"""

cache = set()
# вот тут есть куча варинтов развания собыйти.
cities = {x.strip().lower().replace('ё', 'е') for x in open("cities.txt", "r").readlines() if x.strip()}
wrong_char = ("Ъ", "ь", "ы", "й")
char = None

while True:
    user_say = input(f"[{char}] Start:").strip().lower()
    # пользователь назвал город не с той буквы
    if char and char != user_say[0]:
        print('Wrong citi')
        continue
    # пользователь назвал уже озвученный город
    if user_say in cache:
        print("Already said")
        continue
    # такого города нет в списке известных
    if user_say not in cities:
        print("Unknown city. Try again")
        continue
    # убираем из списка доступных
    cities.remove(user_say)
    # перекидываем город в кэш
    cache.add(user_say)
    # выбираем букву для следующего города
    for char in user_say[::-1]:
        if char in wrong_char:
            continue
        else:
            break
    else:
        raise RuntimeError
    # выбираем город
    for city in cities:
        if city.startswith(char):
            break
    else:
        raise Exception("user win")
    # убираем из списка доступных
    cities.remove(city)
    # перекидываем город в кэш
    cache.add(city)
    print(city)
    # выбираем букву для следующего города
    for char in city[::-1]:
        if char in wrong_char:
            continue
        else:
            break
    else:
        raise RuntimeError
