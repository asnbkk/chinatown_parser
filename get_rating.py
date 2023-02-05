import requests
from utils import get_random_header

# header = get_random_header()

URL = 'https://h5api.m.1688.com/h5/mtop.mbox.fc.common.gateway/1.0/?jsv=2.4.11&appKey=12574478&t=1675580836117&sign=1a6fa5c789e55246f7bf48885250f881&api=mtop.mbox.fc.common.gateway&v=1.0&type=jsonp&isSec=0&timeout=20000&dataType=jsonp&callback=mtopjsonp5&data={"fcGroup":"offer-cbu","fcName":"offerdetail-service","fcArgs":"{\"serviceName\":\"offerSatisfactionService\",\"params\":{\"memberId\":\"b2b-2256983270\",\"sellerId\":2256983270,\"offerId\":656994546410,\"isSignedForTm\":false}}"}'

cookies = {
    '__cn_logon__': "false",
    '__cn_logon__.sig': "i6UL1cVhdIpbPPA_02yGiEyKMeZR2hBfnaoYK1CcrF4",
    '_m_h5_c': "3ffea5c1c55b7176ca9c1a0465f0a6f8_1675531887824;f2e64eed8293b64664ac4a82b9e18648",
    '_csrf_token': "1675522233271",
    '_m_h5_tk': "32c134aba3ca7504f05fb93b1cd41463_1675589407504",
    '_m_h5_tk_enc': "0c2868388bc0020ae59d40cb3889a6b2",
    '_tb_token_': "e43e73eeea815",
    'ali_ab': "5.251.148.84.1671928062683.6",
    'ali-ss': "eyJ1c2VySWQiOm51bGwsImxvZ2luSWQiOm51bGwsInNpZCI6bnVsbCwiZWNvZGUiOm51bGwsIm1lbWJlcklkIjpudWxsLCJfZXhwaXJlIjoxNjc1MzIyNzA1OTU1LCJfbWF4QWdlIjo4NjQwMDAwMH0=",
    'ali-ss.sig': "Rgn5tdbxmRnFM7OBC6SOcpksX7fgUr134Ba_eY0XuhY",
    'alicnweb': "touch_tb_at=1675580785032",
    'cna': "sGULHEGFlRkCAV+Nj+XSYh8G",
    'cookie2': "1a8521126d6936f204cfe1a920547bf9",
    'ctoken': "XQAFwoMxd1qXQllH7iAcnaga",
    'isg': "BIqKeMTG3Rply1HtM5xmuxHz2HYsew7VmkP6uRTDNl1rxyqB_Ate5dAx16sbLIZt",
    'keywordsHistory': "toy",
    'l': "fBjmfrLuTKkf61YFfOfanurza77OSIOYYuPzaNbMi9fP_zCM50rfW6Jh_cTHC36NFsNkR3-uIOvDBeYBcnX7m72YBXViYDkmndLHR35....",
    't': "ce18c59350caa7edf285964f2b093c7c",
    'tfstk': "c4ARBjfj7qURwIB5u_H0LEKtTaEdZtURczsU9C-v3YbT1MFOitAM667nFwIN2qC..",
    'x5secdata': "xbb03ea73843d5ce8b83c088f4546030931675236536a3362248a1620252218abczc2eaa__bx__h5api.m.1688.com:443/h5/mtop.alibaba.alisite.cbu.server.moduleasyncservice/1.0",
    'xlly_s': "1"}

# PROXY = '03.69.149.19:80'

# PROXY = {'https': f'http://{PROXY}',
#         'http': f'http://{PROXY}'}
HEADER = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Host': 'h5api.m.1688.com',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0'
}
r = requests.get(
    URL, 
    cookies=cookies,
    headers=HEADER
)

print(r.text)
