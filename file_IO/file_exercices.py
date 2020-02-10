# # function that takes in 2 params and copies the contents of the first into the second
def copy(file_name, new_file_name):
    with open(file_name) as file:
         data = file.read()

    with open(new_file_name, 'a') as new_file:
        new_file.write(data)

print(copy('haiku.txt', 'text'))

# #function that that wirtes the contents of a doc to  another document in reverse
def copy_and_reverse(file, n_file):
    with open(file) as fil:
        new_data = fil.read()
    with open(n_file, 'a') as f:
        f.write(new_data[::-1])
print(copy_and_reverse('text', 'haiku.txt'))

# function that opens a document and returns a dict with number of rows lines and characters in the text
def statistics(file_name):
    total_lines = 0
    total_words = 0
    total_char = 0
    with open(file_name) as file:
        lines = file.read()
        for line in lines:
            total_lines = len(lines.splitlines())

        for word in line:
            total_words = len(lines.split())
            for char in word:
                total_char = len(lines)
                return dict([('line', total_lines), ('word', total_words), ('char', total_char)])
print(statistics('text'))

# finding and replacing  a word in a file  with another
def find_and_replace(file_n, old_word, new_word_):
    with open(file_n) as  fileNew:
        filedata = fileNew.read()
        filedata1= filedata.replace(old_word, new_word_)
    with open(file_n,'w') as newFile:
        newFile.write(filedata1)
print(find_and_replace('haiku.txt', 'a', 'me'))






