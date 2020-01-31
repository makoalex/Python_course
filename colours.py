import termcolor
text= termcolor.colored('HI THERE', color='green', on_color='on_red', attrs=['blink'])
print(text)

import cowsay
stuff= termcolor.colored(cowsay.cow('Wub you olliez'), color='red')

import pyfiglet
messege= input('enter text')
colour=input('enter colour')
art= pyfiglet.figlet_format(messege, font='starwars')
colured=termcolor.colored(art, colour)
print(colured)

