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

def names_second(text):
    res = re.findall('([А-Я]. [А-Я]. [А-Я][а-я]+(,|!|\?|\.|\;|\:|-| |\)\n))', text)
    for element in res:
        name = element[0].strip(',;:!?-\n).(#^ ')
        print(name)

def names_third(text):
    res = re.findall('([А-Я][а-я]+ [А-Я][а-я]+(,|!|\?|\.|\;|\:|-| |\)\n))', text)
    for element in res:
        name = element[0].strip(',;:!?-\n).(#^ ')
        print(name)
        
def main():
    #filename = input ('Введите название файла с расширением(файл с заготовкой "text.txt"): ')
    print ('Task 1 \nНайти и распечатать на экране все упоминания имен вида "инициал + фамилия": \n')
    names_first(basic('text.txt'))
    print ('\nTask 2 \nНайти в статье вообще все имена (инициалы + фамилия, например, В. И. Наливайко; имя + фамилия, например, Винченцо Бренна): \n')
    names_second(basic('text.txt'))
    names_third(basic('text.txt'))

path = r'C:/Users/sony/Desktop'
projectname = 'Экзамен Имена'
folders = \
[]
def createFolder(path):
	if not os.path.exists(path):
		os.mkdir(fullPath)

fullPath = os.path.join(path,projectname)
createFolder(fullPath)

if __name__ == '__main__':
    main()
