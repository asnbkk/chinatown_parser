import requests
import json
import random
from utils import get_random_header
import sys 

def get_variats(props, attrs):
    variant_list = []
    for i in props[0]['value']:
        attr_list = []
        for attr in attrs:
            if i['name'] in attr:
                prod = attrs[attr]
                res_ = {
                    'price': prod['price'], 
                    'saleCount': prod['saleCount'], 
                    'canBookCount': prod['canBookCount']}
                attr_list.append(res_)
        variant_list.append({**i, 'subvariant': attr_list})
    return variant_list

def get_details(details):
    return [{'name': d['name'], 'values': d['values']} for d in details]

def get_prod_by_link(url):
    # url = sys.argv[1]
    session = requests.Session()
    response = session.get(
            url, 
            verify=False, 
            headers=get_random_header()).text
    body = response.split('<script>')[6]
    start, end = 'window.__INIT_DATA=', '</script>'
    res = json.loads(body.split(start)[-1].split(end)[0])

    product = {}

    sku_model = res['globalData']['skuModel']
    props = sku_model['skuProps']
    attrs = sku_model['skuInfoMap']
    product['variants'] = get_variats(props, attrs)
    product['variant_name'] = props[0]['prop']
    product['subvariant_name'] = props[1]['prop']
    
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
    
    product['title'] = res['globalData']['tempModel']['offerTitle']
    # print(product)
    return(json.dumps(product, indent=4, ensure_ascii=True))
    # return res


if __name__ == '__main__':
    url = sys.argv[1]
    # url = 'https://detail.1688.com/offer/655188856269.html?spm=a26352.13672862.offerlist.5.23bd1e62AN6gHB'
    print(get_prod_by_link(url))
    # res = get_prod_by_link(url)
    # with open("sample_2.json", "w") as outfile:
        # outfile.write(json.dumps(res, indent=4, ensure_ascii=False))