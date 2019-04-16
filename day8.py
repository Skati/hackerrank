n=int(input())
d = dict(input().split() for i in range(n))
names=[]
while True:
    try:
        name = str(input())
        names.append(name)
    except EOFError:
        break
for i in names:
    if i in d:
        print('{}={}'.format(i, d[i]))
    else:
        print('Not found')
