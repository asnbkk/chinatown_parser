from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from proxy.generate_proxy import PROXY
import sys
import time
from utils import get_random_header
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = PROXY

headers = get_random_header()
firefox_options = webdriver.FirefoxOptions()
# setting headers
for key, value in headers.items():
    firefox_options.set_preference(key, value)

# setting prxy
firefox_options.set_preference("network.proxy.type", 1)
firefox_options.set_preference("network.proxy.http", proxy.http_proxy.split(":")[1])
firefox_options.set_preference("network.proxy.http_port", int(proxy.http_proxy.split(":")[2]))
# firefox_profile.set_preference("headless", True)

# firefox_options.headless = True

driver = webdriver.Firefox(options=firefox_options)
driver.set_window_size(1920, 1080)

def get_proper_tab(tabs):
    for index, tab in enumerate(tabs):
        if '买家评价' in tab.text:
            return index
        return 1

def get_review(URL):
    driver.get(URL)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".next-tabs-tab")))
    # try:
        # tabs = driver.find_elements(By.CSS_SELECTOR, '.next-tabs-nav > li')
        # print(tabs)
    # except Exception as e:
        # print(e)
    tabs = driver.find_elements(By.CSS_SELECTOR, '.next-tabs-nav li')
    index = get_proper_tab(tabs)
    child_element = driver.find_elements(By.CSS_SELECTOR, '.next-tabs-nav li')[index]


    driver.execute_script("window.scrollTo(0, 700)")
    child_element.click()

    stars = driver.find_elements(By.CSS_SELECTOR, '.star-num')[0].text
    evaluate_rate = driver.find_elements(By.CSS_SELECTOR, '.evaluate-rate')[0].text
    driver.quit()

    return {
        'stars': stars, 
        'evaluate_rate': evaluate_rate}

if __name__ == '__main__':
    # URL = sys.argv[1]
    URL = 'https://detail.1688.com/offer/693445366035.html?spm=a26352.13672862.offerlist.68.59b81e62U5AsBN'
    print(get_review(URL))