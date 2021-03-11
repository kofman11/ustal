# #алгоритм работает для следующих номеров:
# +79877001505
# 9855355353
# +7 937 799 23 12
# +7(987) 707-30-30
# 78485584
# 242552666
# не работает для номеров:
# 88005355353    - так как 10 цифр
# 88005355353 Вася 9 - так как последняя цифра 9 пойдет в итоговый номер

#import numpy as np

file1 = "number1.txt"
file2 = "number2.txt"

# f = open(file1,'r',encoding = 'utf-8')
# Сократил на одну строчку запись
with open(file1,'r',encoding = 'utf-8') as f:
    a = [line.strip() for line in f]
#f.close()
cifra = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbol = ["-"," ","+","(",")","[","]","\t","\r","\n","_",'"',"'"]
#cifra = np.array(cifra, dtype = str)

b = []
for i in a:
    count = 0
    for j in i:
        if j in cifra:
            count+=1
        if count == 11:
            b.append(i)
            break # Чтобы выходил из цикла

    if count == 10:
        b.append("7"+i) # Добавляем если всего 10 цифр

c = []
for i in b:
    q = ''
    for j in i:
        if j in cifra:
            q+=j
        elif not j in simbol and len(q)>=10:
            break
    if q[0] == '8':
        q = list(q)
        q[0] = '7'
        p = ''
        for i in q:
            p += i
        q = p
    c.append('+'+q)
print(c)

with open(file2, 'w') as f2:
    for i in c:
        f2.write(i + '\n')
