# import library
from bs4 import BeautifulSoup
import requests

#Request to website and download HTML contents
url = 'https://towardsdatascience.com/web-scraping-basics-82f8b5acd45c'
req = requests.get(url)
content = req.text
soup = BeautifulSoup(content)
fp = open("contents.txt","w",encoding='utf-8')
fp.write(content)
fp.close()
