file_path = r'C:\Users\Mako\Desktop\Ny mappe\git_stuff.txt'  # absolute path of the file plus r to produce a raw string and avoid a unicode error
file = open(file_path)
print(file.read())
print(file.read())

doc = open('text')
print(doc.read())
print(doc.read())
doc.seek(0)
""" seek helps us reset the code or jump to a particular part of the code"""
print(doc.read())
doc.seek(2)
print(doc.read())
doc.seek(0)  # reset to the beginning of the code
print(doc.readline()) # read until new line is reached
print(doc.readlines())

