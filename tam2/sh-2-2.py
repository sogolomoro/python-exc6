tale_type=input()
if tale_type == 'sum':
    sum_list = []
    sum_pass = 0
    while True:
        x=input()
        if x == 'end':
            break
            x=0
        sum_list.append(int(x))
    for i in range(0,len(sum_list)):
        sum_pass += sum_list[i]
    print(sum_pass)
elif tale_type=="average":
    sum_list = []
    sum_pass = 0
    j=0
    average_f=0.0
    average_i=0
    p=0
    a=0
    while True:
        x=input()
        j+=1
        if x == 'end':
            break
            x=0
        sum_list.append(int(x))
    for i in range(0,len(sum_list)):
        sum_pass += sum_list[i]
    average=sum_pass/(j-1)
    average_i=int(average)
    average_f=average-average_i
    average_f*=100
    p=average_f-int(average_f)
    if p>= 0.5:
        print(average_i+(int(average_f)/100)+0.01)
    else:
        print(average_i+(int(average_f)/100))
elif tale_type=="gcd":
    numbers=[]
    def BMM(a, b):
        if b == 0:
            return a
        else:
            return BMM(b,a%b)
    while True:
        a=input()
        if a == 'end':
            break
            a=0
        numbers.append(int(a))
    bmm=numbers[0]
    for k in numbers[1::]:
        bmm=BMM(k,bmm)
    print(bmm)
elif tale_type=="lcd":
    def BMM(a, b):
        if b == 0:
            return a
        else:
            return BMM(b,a%b)
    list=[]
    def lcd(list):
        resault = abs(int(list[0]))
        for num in list[1:]:
            resault = (resault * abs(int(num))) // (BMM(resault, abs(int(num))))
        return resault
    while True:
        x=input()
        if x == 'end':
            break
            x=0
        list.append(int(x))
    l=lcd(list)
    print(l)
elif tale_type=="min":
    min=int(input())
    while True:
        x=input()
        if x == 'end':
            break
            x=0
        if int(x)<min:
            min=int(x)
    print(min)
elif tale_type=="max":
    m = int(input())
    while True:
        x = input()
        if x == 'end':
            break
            x = 0
        if int(x) > m:
            m = int(x)

    print(m)
else:
    print("Invalid command")