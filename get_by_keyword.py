import requests
from utils import get_random_header
import time
import random
# time.sleep(random.randint(1,10))
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

keyword = '-'

url = f'https://s.1688.com/selloffer/offer_search.htm?keywords={keyword}&n=y&netType=1%2C11%2C16&spm=a260k.dacugeneral.search.0'
# url = 'https://search.1688.com/service/marketOfferResultViewService?keywords=toy&n=y&netType=1,11,16&spm=a260k.dacugeneral.search.0&async=true&asyncCount=20&beginPage=1&pageSize=60&requestId=GzNJJf8T5n4Nd2876Cz8NE3NekcyC3W64T71669704466552&startIndex=20&pageName=major&sessionId=c2db8c9a55384415b6baa4753d1e0d1e&_bx-v=1.1.20'


# print(proxies)    
# 114.37.207.73:80  
proxy = "119.90.38.34:7890"
# r = requests.get(url, verify=False, headers=get_random_header(), proxies={"http":f"http://{proxy}"})
r = requests.get('http://httpbin.org/ip', timeout=10, headers=get_random_header())
# r = requests.get('http://httpbin.org/ip', timeout=10, proxies={"http":f"http://{proxy}"}, headers=get_random_header(), verify=False)
print(r.text)

# print(get_random_header())

