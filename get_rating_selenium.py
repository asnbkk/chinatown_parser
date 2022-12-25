from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from config import PROXY
import sys

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = PROXY

firefox_profile = webdriver.FirefoxProfile()
# to set proxy for firefox
# firefox_profile.set_preference("network.proxy.type", 1)
# firefox_profile.set_preference("network.proxy.http", proxy.http_proxy.split(":")[0])
# firefox_profile.set_preference("network.proxy.http_port", int(proxy.http_proxy.split(":")[1]))
# firefox_profile.set_preference("headless", True)

firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = True
firefox_options.profile = firefox_profile

driver = webdriver.Firefox(options=firefox_options)
driver.set_window_size(1920, 1080)

def get_review(URL):
    driver.get(URL)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".layout-right")))
    element = driver.find_element(By.CSS_SELECTOR, '.next-tabs-nav > li:nth-child(2)')

    driver.execute_script("window.scrollTo(0, 700)")
    element.click()

    stars = driver.find_elements(By.CSS_SELECTOR, '.star-num')[0].text
    evaluate_rate = driver.find_elements(By.CSS_SELECTOR, '.evaluate-rate')[0].text
    driver.quit()

    return {
        'stars': stars, 
        'evaluate_rate': evaluate_rate}

if __name__ == '__main__':
    url = sys.argv[1]
    get_review(url)
# URL = 'https://detail.1688.com/offer/609602652530.html?spm=a26352.13672862.offerlist.33.38221e62IWOkdJ&cosite=-&tracelog=p4p&_p_isad=1&clickid=3bd2518aaed2456d98343f6429a046b4&sessionid=041a0a524fdef3f3136060143ee800cb'