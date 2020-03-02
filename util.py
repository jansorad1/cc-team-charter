import random

def save_seq(name, li):
    f = open(name, 'w')
    f.write(str(li))
    f.close()

def load_seq_1():
    with open("list") as file: # Use file to refer to the file object

       data = file.read()

       strl = list(data[1:len(data)-1].split(','))
       return [int(x) for x in strl]