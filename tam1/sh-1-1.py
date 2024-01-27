a = input()
b = input()
a = int(a)
b = int(b)
i , j , a2 , b2 , n  = 0 ,0 , 0 , 0 , 0

while 1 <= a:
    a2 = (a % 2) * (10 ** i) + a2
    a = a//2
    i = i + 1
while 1 <= b:
    b2 = (b % 2) * (10 ** j) + b2
    b = b//2
    j = j + 1

while a2>0 or b2>0 :
    x , y = 0 , 0
    x = a2 % 10
    a2 = a2 // 10
    y = b2 % 10
    b2 = b2//10
    if (x!=y):
        n = n + 1
print(n)




