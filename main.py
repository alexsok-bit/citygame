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
cities = {x.strip().lower() for x in open("cities.txt", "r").readlines() if x.strip()}
wrong_char = ("Ъ", "ь", "ы", "й")

while True:
    user_say = input("Start:").strip().lower()
    if user_say not in cities and user_say not in cache:
        print("Wrong city. Try again")
        continue

    cities.remove(user_say)
    cache.add(user_say)

    for c in user_say[::-1]:
        if c in wrong_char:
            continue
        else:
            break
    else:
        raise RuntimeError

    for city in cities:
        if city.startswith(c):
            break
    else:
        raise Exception("user win")

    cities.remove(city)
    cache.add(city)
    print(city)
