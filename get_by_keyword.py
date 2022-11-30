import requests
from utils import get_random_header

keyword = 'toy'
url = f'https://s.1688.com/selloffer/offer_search.htm?keywords={keyword}&n=y&netType=1%2C11%2C16&spm=a260k.dacugeneral.search.0'
# url = 'https://search.1688.com/service/marketOfferResultViewService?keywords=toy&n=y&netType=1,11,16&spm=a260k.dacugeneral.search.0&async=true&asyncCount=20&beginPage=1&pageSize=60&requestId=GzNJJf8T5n4Nd2876Cz8NE3NekcyC3W64T71669704466552&startIndex=20&pageName=major&sessionId=c2db8c9a55384415b6baa4753d1e0d1e&_bx-v=1.1.20'

proxies = {
    "http": "http://121.129.127.209:80",
    "https": "http://121.129.127.209:80"
}

r = requests.get(url, verify=False, headers=get_random_header(), proxies=proxies, stream=True)

# print(r.text)

# ## importing socket module
# import socket
# ## getting the hostname by socket.gethostname() method
# hostname = socket.gethostname()
# ## getting the IP address using socket.gethostbyname() method
# ip_address = socket.gethostbyname(hostname)
# ## printing the hostname and ip_address
# print(f"Hostname: {hostname}")
# print(f"IP Address: {ip_address}")

# print(r.raw._connection.sock.getsockname())
print(r.text)

# headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0',
#         'Accept': '*/*',
#         'Accept-Language': 'en-US,en;q=0.5',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Referer': 'https://s.1688.com/',
#         'Origin': 'https://s.1688.com',
#         'Connection': 'keep-alive',
#         'Cookie': 'l=fBjmfrLuTKkf6H31BOfanurza77OSIOYYuPzaNbMi95P_i1w5uXFW65SYs8eC36NFs92R3-2YAyHBeYBcQd-nxvTjcAEDmHmndLHR35..; tfstk=cWEVBNY50cV5AmqrA0maY9AaMVOAasNgM3lro1XjQi3V-IoI_s0X6YfciYl2UC0c.; cna=sGULHEGFlRkCAV+Nj+XSYh8G; isg=BB8fKoaigFPWB4RO1jOrCIy0rXWphHMmEtSOJrFsu04VQD_CuVQDdp0WAkg-Q0ue; _m_h5_tk=78073b9c63523786df4d218d18288ee3_1669714342029; _m_h5_tk_enc=beb1a069509174098f03f113eb9d887c; xlly_s=1; cookie2=17c9d1ecc0aa614bb7e77761726983c4; t=c5dc8f7589fb0ad966ca8e27f041e9fd; _tb_token_=e76e5e4bba75a; __cn_logon__=false; alicnweb=touch_tb_at%3D1669703902789; keywordsHistory=letter; ali_ab=95.141.143.229.1669703932335.5; _csrf_token=1669704411337',
#         'Sec-Fetch-Dest': 'empty',
#         'Sec-Fetch-Mode': 'cors',
#         'Sec-Fetch-Site': 'same-site',
#         'TE': 'trailers'}