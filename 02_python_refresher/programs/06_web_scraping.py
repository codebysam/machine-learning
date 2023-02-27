import bs4
import requests

res = requests.get("https://en.wikipedia.org/wiki/Machine_learning")
soup = bs4.BeautifulSoup(res.text, 'lxml')

title = soup.select('title')[0].getText()

print(f"Title: {title}")

# headlines = soup.select('span.mw-headline')
headlines = soup.select('div.vector-toc-text')

print("\nHeadlines: ")
for i in headlines:
    print(i.text)

links = soup.find_all('a', href=True)

for i in links:
    print(f"{i.text} ==> {i['href']}")
    