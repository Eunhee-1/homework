import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url ='https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309'
data = requests.get( url ,headers = headers)

soup = BeautifulSoup(data.text, 'html.parser')


musicList = soup.select('#body-content > div.newest-list > div > table > tbody > tr > td.info')

# select를 이용해서, tr들을 불러오기

# movies (tr들) 의 반복문을 돌리기
rank = 1
for music in musicList:
    # movie 안에 a 가 있으면,

    name = music.select_one('a.title.ellipsis')
    musicName = name.text.strip()
    singer = music.select_one('a.artist.ellipsis')
    # print(singer.text.strip())
    if name is not None:
        # a의 text를 찍어본다.
        print (rank, musicName, singer.text)
        rank = rank +1

