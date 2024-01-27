def coded():
    text = inp.split(' ')
    text.sort(key=lambda x: int(x[1:]))
    for i in text:
        print(i[0],end='')
inp=str(input())
coded()