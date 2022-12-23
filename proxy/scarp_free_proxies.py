import requests
from bs4 import BeautifulSoup
import base64
import json

def decode_ip(ip_element):
    ip_temp = ip_element.split('"')[1]
    return str(base64.b64decode(ip_temp))[2:-1]

def get_proxy_list(top, pages):
    for index in range(pages):
        r = requests.get(URL + f'/{index}')
        text = r.text

        soup = BeautifulSoup(text, "html.parser")
        rows = soup \
                .find("tbody") \
                .find_all("tr")

        for row in rows:
            try:
                ip_decoded = row \
                    .find('td', {'class': 'left'}) \
                    .find('script') \
                    .find(text=True)
                ip = decode_ip(ip_decoded)
                port = row \
                    .find('span', {'class': 'fport'}) \
                    .text
                speed = row \
                    .find('div', {'style': 'padding-left:5px'})\
                    .text.strip()[:-3]
                res_ = {'ip': ip, 
                        'port': port, 
                        'speed': int(speed)}
                if res_ not in proxy_list:
                    proxy_list.append(res_)
            except Exception as e:
                print(e)
                pass

    
    proxy_list.sort(key=lambda a: a['speed'])

    with open('./proxy/proxy_list.json', 'w') as f:
        json.dump(proxy_list[:top], f)

    return 0

if __name__ == '__main__':
    URL = 'http://free-proxy.cz/ru/proxylist/country/all/https/ping/all'
    proxy_list = []
    TOP = 10
    PAGES = 10
    get_proxy_list(TOP, PAGES)