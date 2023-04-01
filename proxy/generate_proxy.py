# import random

# host_list = [
#     '212.116.246.202', '91.147.126.179', '185.120.78.201', '46.8.31.101',
#     '109.248.199.58', '185.231.244.18', '89.191.227.27', '109.107.164.240'
# ]

# USERNAME = 'bekkaliyevassan'
# PASS = 'JgMqRpcssL'
# PORT = '49155'


# def get_proxy():
#     HOST = random.choice(host_list)
#     proxy = {
#         'http': f'http://{USERNAME}:{PASS}@{HOST}:{PORT}',
#         'https': f'http://{USERNAME}:{PASS}@{HOST}:{PORT}'
#     }
#     return proxy
def get_proxy():
    proxies = {
        "http": "http://35afaab235284141977868d9ba566eee:@proxy.crawlera.com:8011/",
        "https": "http://35afaab235284141977868d9ba566eee:@proxy.crawlera.com:8011/",
    }
    return proxies
