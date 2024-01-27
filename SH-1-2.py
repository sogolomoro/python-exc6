a=int(input())
b=int(input())
k=int(input())
def add(x, y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x
sum=add(a,b)
print(sum)
if sum==k:
    print('YES')
else:
    print('NO')