a = int(input())
b = int(input())
n = int(input())
i,j=0,0
a2=bin(a)[2:].zfill(32)
b2=bin(b)[2:].zfill(32)
answers=[]
# while 1 <= a:
#     a2 = (a % 2) * (10 ** i) + a2
#     a = a//2
#     i = i + 1
# while 1 <= b:
#     b2 = (b % 2) * (10 ** j) + b2
#     b = b//2
#     j = j + 1
guests_list= list(str(b2)+str(a2))
# print(a2,b2,guests_list)
for w in range(0,n):
    guests_num=int(input())
    if guests_list[-guests_num-1]=='0':
        answers.append('no')
    elif guests_list[-guests_num-1]=='1':
        answers.append('yes')

print(*answers, sep='\n')
