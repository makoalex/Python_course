# HTTP means HYPER TEXT TRANSFER PROTOCOL

# 1. DNS lookup
# 2. pc makes a request to a server (GET OR POST)
# 3. the server receives the request            2, 3, 4 are called the REQUEST/RESPONSE cycle
# 4. the server then issues a response back

# API means application programing interface
# it's a version of a website meant to help computers talk between computers

import requests
url3 ='https://www.spotify.com/no/'
url= 'https://news.ycombinator.com/'
url1= 'https://icanhazdadjoke.com/'
# response= requests.get(url1, headers={'Accept' : 'text/plain'})
response= requests.get('https://icanhazdadjoke.com/', headers={'Accept' : 'application/json'})
data=response.json()
print(data)
print(data['joke'])


# print(response.headers)
# print(response.status_code)
# print(response.content)
# print('your request to {} came back /w status code {}. '.format(url, response.status_code))



