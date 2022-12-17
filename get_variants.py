import json

f = open('./sample_2.json')
res = json.load(f)

sku_model = res['globalData']['skuModel']
props = sku_model['skuProps']
attrs = sku_model['skuInfoMap']

def get_details(details):
    return [{'name': d['name'], 'values': d['values']} for d in details]

get_details(res['data'])

print(res['data'])

# # print(props)
# def get_variats(props, attrs, sku_model):
#     variant_list = []
#     for i in props[0]['value']:
#         attr_list = []
#         for attr in attrs:
#             if i['name'] in attr:
#                 prod = attrs[attr]
#                 try:
#                     price = prod['price']
#                 except:
#                     # seems to be default price for all vars
#                     # todo: price can be shit -
#                     price = sku_model['skuPriceScale']

#                 if '-' in price:
#                     price = price.split('-')[-1]
                
#                 name = prod['specAttrs'].split(';')[-1]
#                     # print('shit schema')
#                 res_ = {
#                     'price': price, 
#                     'name': name,
#                     'saleCount': prod['saleCount'], 
#                     'canBookCount': prod['canBookCount']}
#                 attr_list.append(res_)
#         variant_list.append({**i, 'subvariant': attr_list})
#     return variant_list

# res = get_variats(props, attrs, sku_model)
# print(res)
