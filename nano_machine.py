import requests
import os
from bs4 import BeautifulSoup

def numberator(num):
    if num < 10:
        return f"00{num}"
    
    elif num < 100:
        return f"0{num}"
    
    else:
        return str(num)


url = "https://www.webnovel.com/book/28507722508409805/catalog"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
http = requests.get(url,headers=headers) #for Daotranslate Barbarian ENG
file = f"Nano Machine\\Nano Machine.txt"
# check status code for response received
# success code - 200
print(http)
soup = BeautifulSoup(http.content, 'html.parser')
#s = soup.find('div', class_='text-left') #for Fortune Barbarian RAW
s = soup.find('ol', class_='clearfix g_row content-list mb32') #for Daotranslate Barbarian ENG
content = s.find_all('li')
book = ""

for chapter in content:

    chapter_url = "https://www.webnovel.com"+chapter.find("a")["href"]

    chapter_http = requests.get(chapter_url,headers=headers)

    chapter_soup = BeautifulSoup(chapter_http.content, 'html.parser')

    title = chapter_soup.find('h1', class_='dib mb0 fw700 fs24 lh1.5').text

    book += f"\n {title} \n\n"

    pg = chapter_soup.find('div', class_='cha-words')
    text = pg.find_all("p")

    for sent in text:
        book += f"{sent.text}\n"


    print(title)
    
os.makedirs(os.path.dirname(file), exist_ok=True)
with open(file, "a", encoding="utf-8") as f:
    f.write(book)

