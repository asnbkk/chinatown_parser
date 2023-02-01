import requests
from utils import get_random_header

header = get_random_header()

URL = 'https://h5api.m.1688.com/h5/mtop.mbox.fc.common.gateway/1.0/?jsv=2.4.11&appKey=12574478&t=1675236535794&sign=67d3e64e911623ea31c7d18c37b99fdf&api=mtop.mbox.fc.common.gateway&v=1.0&type=jsonp&isSec=0&timeout=20000&dataType=jsonp&callback=mtopjsonp6&data={"fcGroup":"offer-cbu","fcName":"offerdetail-service","fcArgs":"{\"serviceName\":\"offerSatisfactionService\",\"params\":{\"memberId\":\"b2b-285692572092e25\",\"sellerId\":2856925720,\"offerId\":611079337733,\"isSignedForTm\":false}}"}'

cookies = {
    '__cn_logon__': "false",
    '__cn_logon__.sig': "i6UL1cVhdIpbPPA_02yGiEyKMeZR2hBfnaoYK1CcrF4",
    '_csrf_token': "1675236229143",
    '_m_h5_tk': "c0002f98fd0317bb8473b94fdc5eda88_1675246635569",
    '_m_h5_tk_enc': "60e04f4c823aef0741aca44845b42a86",
    '_tb_token_': "e17148e3007e3",
    'ali_ab': "5.251.148.84.1671928062683.6",
    'ali-ss': "eyJ1c2VySWQiOm51bGwsImxvZ2luSWQiOm51bGwsInNpZCI6bnVsbCwiZWNvZGUiOm51bGwsIm1lbWJlcklkIjpudWxsLCJfZXhwaXJlIjoxNjc1MzIyNzA1OTU1LCJfbWF4QWdlIjo4NjQwMDAwMH0=",
    'ali-ss.sig': "Rgn5tdbxmRnFM7OBC6SOcpksX7fgUr134Ba_eY0XuhY",
    'alicnweb': "touch_tb_at=1673796258038",
    'cna': "sGULHEGFlRkCAV+Nj+XSYh8G",
    'cookie2': "1252342620651bce4a91e8cbbeb522de",
    'ctoken': "XQAFwoMxd1qXQllH7iAcnaga",
    'isg': "BH19A79ywkY_SWb02N0pcvrij993GrFsp6qtvj_CuVQDdp2oB2rBPEsgIDIwbckk",
    'keywordsHistory': "bracelet",
    'l': "fBjmfrLuTKkf64yX4Ofanurza77OSIOYYuPzaNbMi9fP_qCe5EmNW6JwTV8wC36NFsMXR3rfNdDXBeYBcnmF7h2Zb4_3OWMmndLHR35..",
    't': "7af74fead77d282acc98ecf894e687a2",
    'tfstk': "cbCFBVD_TQj_3vfwGCAP3BPAc0wdZ5slvf-wKu_-_h4L7epGiziJSkqH7HuZqpf..",
    'x5secdata': "xbb03ea73843d5ce8b83c088f4546030931675236536a3362248a1620252218abczc2eaa__bx__h5api.m.1688.com:443/h5/mtop.alibaba.alisite.cbu.server.moduleasyncservice/1.0",
    'xlly_s': "1"}

PROXY = '03.69.149.19:80'

PROXY = {'https': f'http://{PROXY}',
        'http': f'http://{PROXY}'}

r = requests.get(
    URL, 
    cookies=cookies,
    headers=header,
    verify=False,
)

print(r.text)
