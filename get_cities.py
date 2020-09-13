#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
#
# Created at 12.09.2020.
# Python 3.7.3 x64
# Contacts: alexandrsokolov@cock.li
#
import requests

URL = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8"

r = requests.get(URL)
with open("cities.html", "w") as f:
    f.write(r.text)
