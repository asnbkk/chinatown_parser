import requests

keyword = 'hello'
url = f'https://s.1688.com/selloffer/offer_search.htm?keywords={keyword}'

r = requests.get(url, verify=False)

print(r.text)