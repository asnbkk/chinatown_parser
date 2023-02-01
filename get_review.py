URL = 'https://detail.1688.com/offer/678205577425.html?spm=a26352.13672862.offerlist.1.6fef1e623npXzD&cosite=-&tracelog=p4p&_p_isad=1&clickid=16d523c135b246409e4b0371bb9c9b82&sessionid=c84818143236f66b1879050e316df244'
#     print(get_review())

import requests

# Enable cookie tracking
session = requests.Session()
adapter = requests.adapters.HTTPAdapter(max_retries=10, pool_connections=100, pool_maxsize=100)
session.mount('https://', adapter)

# Make the request
response = session.get(URL)

# Print the cookies that were sent and received in the request
print("Sent cookies:", session.cookies.items())
print("Received cookies:", response.cookies.items())