#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
#
# Created at 12.09.2020.
# Python 3.7.3 x64
# Contacts: alexandrsokolov@cock.li
#
from bs4 import BeautifulSoup


with open("cities.html", "r") as f:
    html = f.read()

soup = BeautifulSoup(html, features="html.parser")
table = soup.find("table", attrs={"class": "standard sortable"})

with open("cities.txt", "w") as f:
    for row in table.find_all("tr")[2:]:
        city = row.find_all("td")[2].get_text().strip()
        f.write(f"{city}\n")
