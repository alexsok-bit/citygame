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
from itertools import cycle

check_list = []


def normalize_city_name(name):
    return name.strip().lower().replace('ё', 'е')


def check_point(fun):
    check_list.append(fun)
    return fun


@check_point
def is_city_startswith_char(city, char, **kwargs):
    if char is None or city.startswith(char):
        return True
    else:
        print(f'Город должен начинаться с буквы {char.capitalize()}.')
        return False


@check_point
def is_non_cached(city, cache, **kwargs):
    if city not in cache:
        return True
    else:
        print("Этот город уже был назван.")
        return False


@check_point
def is_available(city, cities, **kwargs):
    if city in cities:
        return True
    else:
        print("Я такого города не знаю.")
        return False


def move_to_cache(city, cities, cache):
    # убираем из списка доступных
    cities.remove(city)
    # перекидываем город в кэш
    cache.add(city)


def get_next_char(city):
    wrong_char = ("Ъ", "ь", "ы", "й")
    # выбираем букву для следующего города
    for char in city[::-1]:
        if char in wrong_char:
            continue
        else:
            break
    else:
        raise RuntimeError
    return char


def user_point(char):
    user_say = input(f"[{char or 'any'}] Start:")
    city = normalize_city_name(user_say)
    kw = {"char": char, "cache": cache, "cities": cities}
    if not all(x(city, **kw) for x in check_list):
        return user_point(char)
    return city


def ai_point(char):
    # выбираем город
    for city in cities:
        if city.startswith(char):
            break
    else:
        raise SystemExit("Вы победили!")
    print(city)
    return city


def main():
    char = None
    for point in cycle((user_point, ai_point)):
        next_city = point(char)
        move_to_cache(next_city, cities, cache)
        char = get_next_char(next_city)


if __name__ == '__main__':
    cache = set()
    # вот тут есть куча варинтов развания собыйти.
    cities = {normalize_city_name(x) for x in open("cities.txt", "r").readlines() if x.strip()}
    main()
