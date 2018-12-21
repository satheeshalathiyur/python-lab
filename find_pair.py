'''
findout pairst with sum
ex: l = [11, 15, 6, 8, 9, 10]
    s = 16
    output: [(10,6)]
'''
l = raw_input('enter values seperated by commas')
s = int(raw_input('sum ?'))
l = map(int,l.split(','))
l.sort()
l = [i for i in l if i<s]
p_list = []

for  i in l:
    for j in range(len(l)):
        if i != l[j]:
            if (i+l[j]) == s:
                if (l[j], i) not in p_list:
                    p_list.append((i,l[j]))

print p_list