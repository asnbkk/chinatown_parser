import requests

proxies = {
    "http": 'http://8.210.83.33:80'
}

keyword = 'toy'
url = f'https://s.1688.com/selloffer/offer_search.htm?keywords={keyword}&n=y&netType=1%2C11%2C16&spm=a260k.dacugeneral.search.0'

response = requests.get(url, proxies=proxies, timeout=10)

print(response.text)