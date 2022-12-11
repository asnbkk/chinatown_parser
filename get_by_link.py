import requests
import json
import random
from utils import get_random_header

def get_prod_by_link(url):
    session = requests.Session()
    response = session.get(
            url, 
            verify=False, 
            headers=get_random_header()).text
    body = response.split('<script>')[6]
    start, end = 'window.__INIT_DATA=', '</script>'
    res = json.loads(body.split(start)[-1].split(end)[0])
    
    # print(json.dumps(res, indent=4, ensure_ascii=False))
    return json.dumps(res, indent=4, ensure_ascii=False)

# url = f'https://detail.1688.com/offer/627534969028.html?spm=a26352.13672862.offerlist.20.40d82ab97Hn8h2&cosite=-&tracelog=p4p&_p_isad=1&clickid=ec66899442184bc6b4473873183770bf&sessionid=094d711655c4d7471291943a7d12e7ca'
# print(get_prod_by_link(url))