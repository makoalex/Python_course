# can use it to write into a file, butt it will overwrite and delete the previous context
# it can write into an already existing file or create one automatically

with open('haiku.txt', 'w') as file:
    file.write("The light of a candle\n")
    file.write("It transfered itself to another candle\n")
    file.write("Spring twilight.\n") # that was an example of creating a new  text.

with open ('haha.txt', 'w') as new_doc:
     new_doc.write('hahalolmuhaha\n'*100000)
# if you want to append to an existing file without altering the context we use A instead of W
with open('haiku.txt', 'a') as file:
     file.write("love between us is\n")
     file.write('speachand breath. loving you is+\n')
     file.write('a long river running\n')