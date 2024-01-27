# n=input()
# plan=[]
# map=[]
# while True:
#     x = input()
#     if x == 'END': break
#     if x == ('B'): j+=1
#     plan.append(x)
i = 0
j = 0
n = int(input())
row = []
map1 = []
for c in range(n):
    row.append('.')
for c in range(1000):
    jeff=row.copy()
    map1.append(jeff)
map1[i][j]='*'
command=input()
while command!="END":

    if command=="L":
        if i-1>=0:
            i-=1
        else:
            i=0
    elif command=="R":
        if i < n-1:
            i+=1
        else:
            i = n-1
    elif command=="B":
        j +=1
    map1[j][i]='*'
    command=input()

while True:
    if row in map1:
        map1.pop(map1.index(row))
    else:
        break
for m in range(len(map1)):
    for K in range(n):
        print(map1[m][K],end=' ')
    print('\n')

if i != n-1:
    print("There's no way out!")

