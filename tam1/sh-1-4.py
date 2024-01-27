a,b=map(int,input().split())
w=0
if 0<=a<=1000 and 0<=b<=1000:
    if a <= b:
        for i in range(a, b + 1):
            k = 0
            if i>1:
                for r in range(2, int(i / 2) + 1):
                    if i % r == 0:
                        k = 1
                        break
                if k == 0:
                    w += 1
        print("main order - amount:", w)

    else:
        for i in range(b, a + 1):
            k = 0
            if i > 1:
                for r in range(2, int(i / 2) + 1):
                    if i % r == 0:
                        k = 1
                        break
                if k == 0:
                    w += 1

        print("reverse order - amount:", w)









