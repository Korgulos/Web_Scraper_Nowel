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


for chapter in range(87, 256):
    # Making a GET request
    # http = requests.get(f'https://www.fortuneeternal.com/novel/surviving-the-game-as-a-barbarian-raw/chapter-{chapter}/') #for Fortune Barbarian RAW
    http = requests.get(
        f"https://etudetranslations.com/novel/from-goblin-to-goblin-god/chapter-{chapter}/"
    )  # for Daotranslate Barbarian ENG
    barbarian_file = f"From Goblin to Goblin God\\{numberator(chapter)} - Chapter.txt"
    # check status code for response received
    # success code - 200
    print(http)
    soup = BeautifulSoup(http.content, "html.parser")
    # s = soup.find('div', class_='text-left') #for Fortune Barbarian RAW
    s = soup.find("div", class_="text-left")  # for Daotranslate Barbarian ENG
    content = s.find_all("p")
    # translated = ""
    text = ""

    # for line in content:
    #     #to_english = GoogleTranslator(source='auto', target='en').translate(str(line)) #for Fortune Barbarian RAW
    #     translated += f"{str(line)} \n"
    # translated = translated.replace("</p>", "").replace("<p>", "")
    # print(translated)
    for c in content:
        text += f"{str(c)} \n"
        text = text.replace("</p>", "").replace("<p>", "")

    print(text)
    os.makedirs(os.path.dirname(barbarian_file), exist_ok=True)

    with open(barbarian_file, "x", encoding="utf-8") as f:
        f.write(text)
