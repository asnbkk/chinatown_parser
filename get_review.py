# import requests
# from utils import get_random_header
# import json
# from bs4 import BeautifulSoup
# header = get_random_header()

# # # def get_cookies():
# # #     URL = ''
# # #     session = requests.Session()
# # #     response = session.get(URL)
# # #     print(response.cookies)

# # # get_cookies()
# cookies = {
#     '_m_h5_tk':"b05fc4955e869e6676eb25e476a66759_1671975591618",
#     '_m_h5_tk_enc':"cf922b2d6a453e9c69c2b393c27b8606"}

# def get_review():
#     r = requests.get(URL, cookies=cookies).text.split('(')[1].split(')')[0]
#     # res = json.loads(r)['data']['model']
#     # return {
#     #     'good_rate': res['goodRates'],
#     #     'goods_grade': res['goodsGrade'],
#     # }
#     return r
    
# if __name__ == '__main__':
URL = 'https://h5api.m.1688.com/h5/mtop.1688.trade.service.mtoprateservice.querydsrratedatav2/1.0/?jsv=2.4.11&appKey=12574478&t=1671965519185&sign=e8fc1d5d550c57f1908f2053c3b1281e&api=mtop.1688.trade.service.MtopRateService.queryDsrRateDataV2&v=1.0&type=jsonp&isSec=0&timeout=20000&dataType=jsonp&callback=mtopjsonp6&data={"offerId":691028434415,"loginId":"东莞市正宇鞋业有限公司","scene":"item"}'
#     print(get_review())

import requests
import http.cookies

# Enable cookie tracking
session = requests.Session()
adapter = requests.adapters.HTTPAdapter(max_retries=10, pool_connections=100, pool_maxsize=100)
session.mount('https://', adapter)

# Make the request
response = session.get(URL)

# Print the cookies that were sent and received in the request
print("Sent cookies:", session.cookies.items())
print("Received cookies:", response.cookies.items())