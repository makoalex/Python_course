# import requests
# url='https://icanhazdadjoke.com/search'
# user_input= input('what category would you like ?').strip().lower()
# results=requests.get(url,
#                      headers={'Accept': 'application/json'},
#                      params={'term' : user_input, 'limit':1}
# )
# data= results.json()
# print(data)
# print(data['results'])

import termcolor
import pyfiglet
from random import choice
import requests
user_input = input('Mako wants to tell you a joke! Pick a topic!').lower().strip()
text=user_input+'joke 101'

message = pyfiglet.figlet_format(text, font='starwars')
art = termcolor.colored(message, color='red')
url = 'https://icanhazdadjoke.com/search'
print(art)


result = requests.get(url,
                      headers={'Accept': 'application/json'},
                      params={'term': user_input}
                      ).json()
number_jokes = result['total_jokes']
final_result = result['results']

if number_jokes > 1:
    print("I found {} jokes matching your criteria: {}! Here is one: ".format(number_jokes, user_input))
    print(choice(final_result)['joke'])
elif number_jokes == 1:
    print(" I found one joke matching your criteria: {}! Here is it is: ".format(user_input))
    print(final_result[0]['joke'])
else:
    print("I found no matches for {}".format(user_input))
