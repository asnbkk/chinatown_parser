import requests

response = requests.get(
    "https://api.myip.com/",
    proxies={
        "http": "http://35afaab235284141977868d9ba566eee:@proxy.crawlera.com:8011/",
        "https": "http://35afaab235284141977868d9ba566eee:@proxy.crawlera.com:8011/",
    },
    verify='./zyte-proxy-ca.crt'
)
print(response.text)
