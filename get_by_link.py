import requests
import json
import random
from utils import get_random_header
import sys 

def get_details(details):
    return [{'name': d['name'], 'values': d['values']} for d in details]

def get_prod_by_link(url):
    url = sys.argv[1]
    session = requests.Session()
    response = session.get(
            url, 
            verify=False, 
            headers=get_random_header()).text
    body = response.split('<script>')[6]
    start, end = 'window.__INIT_DATA=', '</script>'
    res = json.loads(body.split(start)[-1].split(end)[0])
    
    product = {}
    for key, value in res['data'].items():
        if type(value) is not bool and type(value) is not list:
            try:
                if value['componentType'] == '@ali/tdmod-od-pc-offer-price':
                    product['prices'] = value['data']['priceModel']['currentPrices']
                elif value['componentType'] == '@ali/tdmod-od-pc-attribute-new':
                    product['details'] = get_details(value['data'])
            except KeyError or TypeError:
                continue
    
    for image in res['globalData']['images']:
        imageList = []
        imageList.append({
            'url': image['fullPathImageURI'],
            'preview': image['size220x220ImageURI'],
        })
        product['images'] = imageList
    
    # print(product)
    product['title'] = res['globalData']['tempModel']['offerTitle']
    return(json.dumps(product, indent=4, ensure_ascii=True))


if __name__ == '__main__':
    url = sys.argv[1]
    # url = 'https://detail.1688.com/offer/692256621725.html?spm=a26352.13672862.offerlist.30.714b32c0fwVgA8&cosite=-&tracelog=p4p&_p_isad=1&clickid=bd938112b7744611977c680aef698af6&sessionid=893d0c70911a57cdd0f7b3b1621d375c'
    print(get_prod_by_link(url))
    # res = get_prod_by_link(url)
    # with open("sample_2.json", "w") as outfile:
        # outfile.write(json.dumps(res, indent=4, ensure_ascii=False))