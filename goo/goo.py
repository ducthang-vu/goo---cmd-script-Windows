#! python3
import sys
import webbrowser
import requests
import bs4
import os
import os.path


def accepting(string, list_):
    return any([item for item in list_ if item in string])


# getting accepted keywords from goo.txt
text_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'goo.txt')
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
