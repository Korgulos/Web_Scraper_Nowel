import requests
import os
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator


def numberator(num):
    if num < 10:
        return f"00{num}"

    elif num < 100:
        return f"0{num}"

    else:
        return str(num)


barbarian = ""

for chapter in range(1, 256):
    barbarian_file = f"From Goblin to Goblin God\\{numberator(chapter)} - Chapter.txt"

    with open(barbarian_file, "r", encoding="utf-8") as f:
        barbarian += f"{f.read()} \n \n --- \n \n"


with open("From Goblin to Goblin God.txt", "x", encoding="utf-8") as f:
    f.write(barbarian)
