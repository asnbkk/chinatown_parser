import random
import requests
import json

def get_random_proxy():
    f = open('./proxy/proxy_list.json')
    data = json.load(f)
    random_proxy = random.choice(data)
    proxy = f"{random_proxy['ip']}:{random_proxy['port']}"
    return proxy, random_proxy['speed']

while True:
    # proxy = get_random_proxy()[0]
    proxy = 'marinaneymar13:VxPkMUVIHL@212.116.244.228:49155'

    PROXY = {'https': f'https://{proxy}',
            'http': f'http://{proxy}'}

    # print(f'Using proxy: {proxy} with speed {get_random_proxy()[1]}')
    try:
        with requests.Session() as session:
            session.proxies = PROXY
            r = session.get('http://ip-api.com/json', timeout=30)
            print(json.dumps(r.json(), indent=2))
    except Exception as e:
        print(e)
        pass