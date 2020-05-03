#! python3
import sys
import webbrowser
import requests
import bs4


def accepting(string, list_):
    return any([item for item in list_ if item in string])


# getting accepted keywords from goo.txt
text_path = r'' #full path of goo.txt inside the inverted commas, for example C:\Users\andrea\goo\goo.txt. 
accepted = open(text_path).read().split(',')

# getting variables from cmd
args = sys.argv[1:]
if not args:
    raise Exception('No argument was passed.')

# requesting google page
url = 'https://www.google.it/search?hl=it&q=' + '+'.join(args)
res = requests.get(url)
res.raise_for_status()

# getting links
soupObject = bs4.BeautifulSoup(res.text, 'html.parser')
links = [item.get('href') for item in soupObject.select('.kCrYT > a') if accepting(item.get('href'), accepted)]

# opening browser tabs
webbrowser.open(url)
for i in reversed(range(min(5, len(links)))):
    webbrowser.open('https://google.com' + links[i])
