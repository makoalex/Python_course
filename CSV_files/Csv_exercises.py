# write a function that takes in a first and last name and adds it to a new file
# from csv import reader, writer, DictReader
# #
# #
# # def add_user(first_name, last_name, country, style, weight):
# #     return first_name, last_name, country, style, weight
# #
# #
# # with open('Tekken_fighters.csv', 'a', newline="") as file:
# #     open_file = writer(file)
# #     open_file.writerow(add_user('claudio', 'Serafino', 'Italy', 'sirius', 87))
# #
# # # printing all the first and last names from the tekken fighters file
# #
# # def solution(s):
# #     for i in s:
# #         if s%2 ==0:
# #             return slice(0,None,2)

n = int(input().strip())
if n %2 ==1:
    print('Weird')
elif n %2 in range(2,6)==0:
    print('Not Weird')
elif n%2 in range(6,21,2) ==0:
    print('weird')
else:
    print('Not Weird')



