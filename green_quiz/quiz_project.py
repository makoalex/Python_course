from csv import DictWriter

with open('quiz.csv', 'a', newline="") as file:
    headers = [' QUESTION ', ' OPTION I ', ' OPTION II ', ' OPTION III ', ' OPTION IV ']
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writerow({
        ' QUESTION ': 'Which of the fallowing is a synonym for naive?',
        ' OPTION I ': 'QUICK- WITTED',
        ' OPTION II ': 'SLIM- FIGURED',
        ' OPTION III ': 'CREDULOUS',
        ' OPTION IV ': 'RIPE'
    })
