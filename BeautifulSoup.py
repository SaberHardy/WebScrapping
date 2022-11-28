from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

url = "http://olympus.realpython.org/"

page = urlopen(url + '/profiles')
html = page.read().decode('utf-8')

soup = bs(html, 'html.parser')

# This will return to you all links that starts with " a "
all_a = soup.find_all('a')

for link in all_a:
    link_url = url + link['href']
    print(link_url)
