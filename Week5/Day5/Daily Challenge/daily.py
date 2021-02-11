
# Using the modules requests and time create a function that returns how long a webpage takes to load (how long it takes for a complete response to a request)
# Test your code with multiple sites such as google, ynet, imdb, etc.

import requests
import time

url1 = 'https://www.google.com'
url2 = 'https://www.ynetnews.com/category/3082'
url3 = 'https://www.imdb.com'


url1_start = time.process_time()
reponse = requests.get(url1)
url1_stop = time.process_time()
url1_final = url1_stop - url1_start
print("Passed time - url1: ",url1_final)

url2_start = time.process_time()
reponse = requests.get(url2)
url2_stop = time.process_time()
url2_final = url2_stop - url2_start
print("Passed time - url1: ",url2_final)


url3_start = time.process_time()
reponse = requests.get(url3)
url3_stop = time.process_time()
url3_final = url3_stop - url3_start
print("Passed time - url1: ",url3_final)


