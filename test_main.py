import sys

from get_by_link import get_prod_by_link

url = sys.argv[1]
# url = f'https://detail.1688.com/offer/627534969028.html?spm=a26352.13672862.offerlist.20.40d82ab97Hn8h2&cosite=-&tracelog=p4p&_p_isad=1&clickid=ec66899442184bc6b4473873183770bf&sessionid=094d711655c4d7471291943a7d12e7ca'
print(get_prod_by_link(url))