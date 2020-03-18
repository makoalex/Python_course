from csv import DictWriter

with open('quiz.csv', 'a', newline="") as file:
    headers = [' QUESTION ', ' OPTION I ', ' OPTION II ', ' OPTION III ', ' OPTION IV ']
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writerow({
        ' QUESTION ': 'Where is a GREEN MOUNTAIN BOY from?',
        ' OPTION I ': 'VERMONT',
        ' OPTION II ': 'BRITISH COLUMBIA',
        ' OPTION III ': 'HAWAII',
        ' OPTION IV ': 'IRELAND'
    })
