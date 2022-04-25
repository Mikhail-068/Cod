from config import dic_table

example = r"\320\237\320\276\320\263\320\276\320\264\320\260.py".split('.')[0]

list_ex = []
temp = []
# for i in range(4):
#     temp.append(example[i])
#     if i % 4 == 0:
#         list_ex.append(''.join(temp))
#         temp = []
for i in range(8):
    temp.append(example[i])
    t = ''.join(temp)
list_ex.append(t)

print(t)
print(list_ex)


