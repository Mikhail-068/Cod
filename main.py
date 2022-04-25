from config import dic_table

def Cod(example):
    list_ex = []
    temp = 0
    for i in range(len(example)):
        if (i != 0) and (i % 8 == 0):
            list_ex.append(example[temp:i])
            temp = i
    words = []
    for i in list_ex:
        words.append(dic_table[i])
    text = ''.join(words)
    print(text)

Cod(input('Введите текст:\n'))