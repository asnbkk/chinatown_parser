import requests
import json
from utils import get_random_header
import sys 
from config import PROXY

def get_variats(props, attrs, sku_model):
    variant_list = []
    for i in props[0]['value']:
        attr_list = []
        for attr in attrs:
            if i['name'] in attr:
                prod = attrs[attr]
                try:
                    price = prod['price']
                except:
                    # seems to be default price for all vars
                    # todo: price can be shit -
                    price = sku_model['skuPriceScale']

                if '-' in price:
                    price = price.split('-')[-1]
                
                name = prod['specAttrs'].split(';')[-1]
                    # print('shit schema')
                res_ = {
                    'price': price, 
                    'name': name,
                    'saleCount': prod['saleCount'], 
                    'canBookCount': prod['canBookCount']}
                attr_list.append(res_)
        variant_list.append({**i, 'subvariants': attr_list})
    return variant_list

def get_details(details):
    return [{'name': d['name'], 'values': d['values']} for d in details]

def get_prod_by_link(url, PROXY=None):
    # url = sys.argv[1]
    session = requests.Session()
    PROXY = {'https': f'http://{PROXY}',
            'http': f'http://{PROXY}'}

    response = session.get(
        url, 
        verify=False, 
        headers=get_random_header(),
        proxies=PROXY).text

    body = response.split('<script>')[6]
    start, end = 'window.__INIT_DATA=', '</script>'
    res = json.loads(body.split(start)[-1].split(end)[0])

    product = {}

    sku_model = res['globalData']['skuModel']
    props = sku_model['skuProps']
    attrs = sku_model['skuInfoMap']
    product['variants'] = get_variats(props, attrs, sku_model)
    
    try:
        product['variant_name'] = props[0]['prop']
        product['subvariant_name'] = props[1]['prop']
    except:
        product['subvariant_name'] = props[0]['prop']
        product['variant_name'] = 'default'
    
    product['prices'] = res['globalData']['orderParamModel']['orderParam']['skuParam']
    
    for key, value in res['data'].items():
        if type(value) is not bool and type(value) is not list:
            try:
                # if value['componentType'] == '@ali/tdmod-od-pc-offer-price':
        
                if value['componentType'] == '@ali/tdmod-od-pc-attribute-new':
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
    product['saled_count'] = res['globalData']['tempModel']['saledCount']
    # print(product)
    return(json.dumps(product, indent=4, ensure_ascii=False))
    # return res


if __name__ == '__main__':
    # url = sys.argv[1]
    url = 'https://detail.1688.com/offer/609602652530.html?spm=a26352.13672862.offerlist.33.38221e62IWOkdJ&cosite=-&tracelog=p4p&_p_isad=1&clickid=3bd2518aaed2456d98343f6429a046b4&sessionid=041a0a524fdef3f3136060143ee800cb'
    res = get_prod_by_link(url, PROXY)
    print(res)
    # with open("sample_1.json", "w") as outfile:
        # outfile.write(json.dumps(res, indent=4, ensure_ascii=False))