import bs4
import requests

url = 'https://sgsikorski.github.io/SpruceLocks'

doc = requests.get(url)

print (bs4.BeautifulSoup(doc.text, "html.parser"))


