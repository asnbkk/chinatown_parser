# import requests
from utils import get_random_header
import json
from bs4 import BeautifulSoup
header = get_random_header()

# # def get_cookies():
# #     URL = ''
# #     session = requests.Session()
# #     response = session.get(URL)
# #     print(response.cookies)

# # get_cookies()
# cookies = {
#     '_m_h5_tk':"5a50a81da75dd47a7b265379c0a5a70f_1671920642406",
#     '_m_h5_tk_enc':"b6107454d62df1fe3c8b9f7c25337511"}

# def get_review():
#     r = requests.get(URL, headers=header, cookies=cookies).text.split('(')[1].split(')')[0]
#     res = json.loads(r)['data']['model']
#     return {
#         'good_rate': res['goodRates'],
#         'goods_grade': res['goodsGrade'],
#     }

# if __name__ == '__main__':
#     URL = 'https://h5api.m.1688.com/h5/mtop.1688.trade.service.mtoprateservice.querydsrratedatav2/1.0/?jsv=2.4.11&appKey=12574478&t=1671913572566&sign=1284203c342a435b92eb62882ab95d71&api=mtop.1688.trade.service.MtopRateService.queryDsrRateDataV2&v=1.0&type=jsonp&isSec=0&timeout=20000&dataType=jsonp&callback=mtopjsonp7&data={"offerId":609602652530,"loginId":"诺富实业公司","scene":"item"}'
#     print(get_review())

import requests

url = 'https://detail.1688.com/offer/609602652530.html?spm=a26352.13672862.offerlist.33.38221e62IWOkdJ&cosite=-&tracelog=p4p&_p_isad=1&clickid=3bd2518aaed2456d98343f6429a046b4&sessionid=041a0a524fdef3f3136060143ee800cb'

response = requests.get(url).text

soup = BeautifulSoup(response, "html.parser")

# product_title = soup.find("div", {"class": "star-info"})

print(response)




