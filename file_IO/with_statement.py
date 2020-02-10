# replaces the method previously studied with a simpler syntax
with open('text') as file:
    print(file.readline())
# we can save the file.read into a variable
with open('text') as f:
    data = f.read()
    print(data)
