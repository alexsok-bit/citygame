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

check_list = []


def normilize_city_name(name):
    return name.strip().lower().replace('ё', 'е')


def proverka(fun):
    check_list.append(fun)
    return fun


@proverka
def is_startswith_true(city, char, **kwargs):
    if char is None or city.startswith(char):
        return True
    else:
        print(f'Город должен начинаться с буквы {char}.')
        return False


@proverka
def is_non_cached(city, cache, **kwargs):
    if city not in cache:
        return True
    else:
        print("Этот город уже был назван.")
        return False


@proverka
def is_alwailable(city, cities, **kwargs):
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
    # выбираем букву для следующего города
    for char in city[::-1]:
        if char in wrong_char:
            continue
        else:
            break
    else:
        raise RuntimeError
    return char


def main():
    char = None
    while True:
        user_say = input(f"[{char or 'any'}] Start:")
        next_city = normilize_city_name(user_say)
        if not all(x(next_city, char=char, cache=cache, cities=cities) for x in check_list):
            continue
        move_to_cache(next_city, cities, cache)
        char = get_next_char(next_city)
        # выбираем город
        for city in cities:
            if city.startswith(char):
                break
        else:
            raise Exception("Вы победили!")
        move_to_cache(city, cities, cache)
        print(city)
        char = get_next_char(city)


if __name__ == '__main__':
    cache = set()
    # вот тут есть куча варинтов развания собыйти.
    cities = {normilize_city_name(x) for x in open("cities.txt", "r").readlines() if x.strip()}
    wrong_char = ("Ъ", "ь", "ы", "й")
    main()
