with open('myfile.txt') as f:
    myfile_text = f.read()

myfile_text_plus_hello = myfile_text + "\nHello from fileio.py!!"

with open('testwrite.txt', 'w') as f:
    f.write(myfile_text_plus_hello)

