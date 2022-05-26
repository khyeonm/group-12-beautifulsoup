# -*- coding: utf-8 -*-
"""크롤링 과제(환율)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16yxiWlwNLX_EQrRDp3NxaeCZcwGkCUyA
"""
#구민주 학생 
!pip install beautifulsoup4
!pip install requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pandas as pd


home='http://finance.naver.com'
url = home+"/marketindex/"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
iframe_src = soup.select_one("#frame_ex1").attrs["src"]
html = urlopen(home+f"{iframe_src}")
soup = BeautifulSoup(html, "html.parser")

table=soup.find("table","tbl_exchange")
tbody=table.find("tbody")
trs=tbody.find_all("tr")

header=["통화명","매매기준율","사실때","파실때","보내실때","받으실때","미화환산율"]
print(header)
result=[]
country=[]
for tr in trs:
    tds=tr.find_all("td")
    data=[]
    for td in tds:
        data.append(td.get_text().strip())
    result.append(data)
    country.append(data[0])
    print(data)
   
#여기부터는 김현민 학생 작성
print("----End of List----") 
print("")

Exchange_rate_trend = input("<<위 리스트에서 앞에 있는 5개 국가 - 미국, 유럽연합, 일본, 홍콩, 중국 >> 중 추이를 알고자하는 국가를 입력해주세요 >")

graph = "#content > div.spot > div.flash_area > img"
url_ = url+"exchangeDetail.naver?marketindexCd=FX_"

#국가별 환율 변동 추이 그래프 (2022.05.24 20:00 하나은행 기준)
if Exchange_rate_trend == "미국":
  Url = url_+"USDKRW" 
  html = urlopen(Url)
  soup = bs(html,"html.parser")
  img = soup.select_one(graph)['src']
  print(f'링크를 누르시면 그래프가 나옵니다>> {img}')
elif Exchange_rate_trend == "유럽연합":
  Url = url_+"EURKRW" 
  html = urlopen(Url)
  soup = bs(html,"html.parser")
  img = soup.select_one(graph)['src']
  print(f'링크를 누르시면 그래프가 나옵니다>> {img}')
elif Exchange_rate_trend == "일본":
  Url = url_+"JPYKRW" 
  html = urlopen(Url)
  soup = bs(html,"html.parser")
  img = soup.select_one(graph)['src']
  print(f'링크를 누르시면 그래프가 나옵니다>> {img}')
elif Exchange_rate_trend == "홍콩":
  Url = url_+"HKDKRW" 
  html = urlopen(Url)
  soup = bs(html,"html.parser")
  img = soup.select_one(graph)['src']
  print(f'링크를 누르시면 그래프가 나옵니다>> {img}')
else:
  Url = url_+"CNYKRW" 
  html = urlopen(Url)
  soup = bs(html,"html.parser")
  img = soup.select_one(graph)['src']
  print(f'링크를 누르시면 그래프가 나옵니다>> {img}')
