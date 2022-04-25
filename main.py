from config import dic_table

example = r"\320\237\320\276\320\263\320\276\320\264\320\260.py"

list_ex = []
temp = 0
for i in range(len(example)):
    if (i != 0) and (i % 8 == 0):
        list_ex.append(example[temp:i])
        temp = i

print(dic_table[list_ex[0]])



