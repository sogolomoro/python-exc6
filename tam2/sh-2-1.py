n=int(input())
def kh_p_T(n):
    for i in range(0,n):
        for j in range(0,i+1):
            if j==0 or i==0:
                c=1
            else:
                c=c*(i-j+1)//j
            print(f"{c} ",end="")
        print(" ")
kh_p_T(n)
