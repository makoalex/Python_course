x=0
for num in range(10,21):
    if num %2!=0:
        x=x+num
        print(x)

print('How many times have i told you that i love you today?  ')
answer=int(input())
for  i in range(answer):
    print('time {}: i love you very very very much'.format(i))

for number in range (1,21):
    if number==4 or  number==13:
        fact='unlucky'
    elif number%2==0:
        fact='even'
    else:
        fact='odd'
    print('{} is {}. '.format(number, fact))
#while loop



num=1

while num:
    num =num+1
    if num==11:
        break
    else:
        pass
    print(num)

