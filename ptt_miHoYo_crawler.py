import requests
from bs4 import BeautifulSoup



url = "https://www.ptt.cc/bbs/miHoYo/index.html"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
response = requests.get(url , headers=headers)#爬下來的網頁
soup = BeautifulSoup(response.text ,features="html.parser")#parser解釋器

articles = soup.find_all(name="div", class_="r-ent")

for a in articles:
    title = a.find("div",class_="title") #用F12找title,類型=div
    if title and title.a:
        title = title.a.text #如果有標題,讓title變成標題
    else:
        title = "沒有標題"


    popular = a.find("div", class_="nrec")
    if popular and popular.span: #F12中找到屬性為span
        popular = popular.span.text
    else:
        popular = "N/A"


    date = a.find("div", class_="date")
    if date:
        date = date.text
    else:
        date = "N/A"
    print(f"標題:{title} 人氣:{popular} DATE:{date}")


# html方法response.text
# print(response.text)

# if response.status_code == 200:
#     with open('output.html' , 'w' , encoding='utf-8') as f:
#         f.write(response.text)
#     print("寫入成功!")
# else:
#     print("沒有抓到網頁")