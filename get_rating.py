import requests
from proxy.generate_proxy import get_proxy
from utils import get_random_header

url = 'https://detail.1688.com/offer/695187062527.html?spm=a260k.dacugeneral.home2019rec.23.663335e41iffsi&&scm=1007.21237.280932.0&pvid=cd9ef994-5c88-44ef-a97c-4d4b574c45f5&object_id=695187062527&udsPoolId=2274586&resourceId=1797996&resultType=normal'
params = {
    'jsv': '2.7.0',
    'appKey': '12574478',
    't': '1680431101627',
    'sign': '7b71ecee72c923c238cebb776f902de2',
    'api': 'mtop.mbox.fc.common.gateway',
    'v': '1.0',
    'type': 'json',
    'isSec': '0',
    'data': '{"fcGroup":"offer-cbu","fcName":"offerdetail-service","fcArgs":"{\\"serviceName\\":\\"offerSatisfactionService\\",\\"params\\":{\\"memberId\\":\\"b2b-332428333580fdb\\",\\"sellerId\\":3324283335,\\"offerId\\":570204643781,\\"isSignedForTm\\":true}}"}'
}

header = get_random_header()
header.update({'Referer': 'https://detail.1688.com/',
              'Host': 'h5api.m.1688.com'})

cookies = {
    '__cn_logon__': 'false',
    '__mwb_logon_id__': 'undefined',
    '_csrf_token': '_csrf_token',
    '_m_h5_tk_enc': 'e2c363e88d61b11975e87e0ab36db433',
    '_m_h5_tk': 'd38a5e54ef70b6b8d0fd62167eefa134_1680446026799',
    '_tb_token_': 'e3e7ee4abe64a',
    'cna': 'pl2IHFhM+BYCAV+Nj+WXSAJ5',
    'cookie2': '186bcb57ebeddb9d49552404485c7bf1',
    'isg': 'BAYG5EeHnjgl3Ep0TztlaJ8vVPqIZ0ohhhexkvAv4ikE86YNWPHXMRXLy7c_wEI5',
    'l': 'fB_f0VMrNQcoTEGEBOfanurza77O7IOYYuPzaNbMi9fP_k1W5Nf1W1i_M58XCn6NFs6MR3-uIn39BeYBc61InxvO7VQ4dJMmndLHR35..',
    'tfstk': 'cfycB0wdC4TBorqqNrMfLR2QwreGafvZ-RPUUgF27_2KPGwr4sfyaBkAjgmORZR1.',
    't': '145a56430e3510acb629c1e0a9ba3ba7',
    'xlly_s': '1'
}

r = requests.get(url,
                 proxies=get_proxy(),
                 verify='./proxy/zyte-proxy-ca.crt')

print(r.text)
