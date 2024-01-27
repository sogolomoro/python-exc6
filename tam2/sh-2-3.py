# def con_base(l,n):
#     i=0
#     a2=0
#     while n-1 <= l:
#         a2 = (l % n) * (10 ** i) + a2
#         l = l // n
#         i = i + 1
#     return a2
# l=0
# sum=0
# k=0
# listt=[]
# while True:
#     a,b=map(int,input().split())
#     if b !=-1: n=b
#     if (n < 2 or n > 9):
#         k+=1
#     if a==-1 or b==-1:
#         break
#     l=0
#     for i in range(1, a + 1):
#         if a % i == 0:
#             l+=a//i
#     sum+=(con_base(l,n))
# if k==0:
#     print(sum)
# else:print('invalid base!')
def binbasen(num, base):
    result = ""
    while num > 0:
        tmpbin = num % base
        result = str(tmpbin) + result
        num //= base
    return result


list1 = []
checkbase = 0
while True:
    tmp = 0
    num, base = map(int, input().split())

    if int(num) + int(base) == -2:
        if checkbase > 0:
            print('invalid base!')
            exit()
        elif checkbase == 0:
            break
    if base < 2 or base >= 10:
        checkbase += 1
    for i in range(1, num + 1):
        if num % i == 0:
            tmp += (num // i)

    list1.append(binbasen(tmp, base))

finalans = 0
for i in range(len(list1)):
    finalans += int(list1[i])
print(finalans)