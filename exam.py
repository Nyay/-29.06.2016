import re
import os

def basic (filename):
    f = open(filename, 'r', encoding = 'UTF-8') 
    text = f.read()
    f.close
    return text

def names_first(text):
    res = re.findall('([А-Я]. [А-Я][а-я]+(,|!|\?|\.|\;|\:|-| |\)\n))', text)
    for element in res:
        name = element[0].strip(',;:!?-\n).(#^ ')
        print(name)

names_first(basic('text.txt'))
