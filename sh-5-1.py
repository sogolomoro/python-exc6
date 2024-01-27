class Crab:
    def __init__(self, dna):
        self.dna = self.encode(dna)

    def encode(self, dna):
        return dna + dna[:10]

    def transcode(self):
        res = ''
        i = 0
        n = len(self.dna) - 1
        while i < n:
            if self.dna[i] == 't' and self.dna[i+1] == 't':
                res += 'o'
                i  += 2
                continue
            res += self.dna[i]
            i += 1
        return res + self.dna[-1]


class SpongeBob(Crab):
    def transcode(self):
        sorted = self.mergesort(self.dna)
        res = ''
        for i in sorted:
            res += i
        return res

    def mergesort(self, l):
        n = len(l)
        if n == 1:
            return  l
        l1 = l[:n // 2]
        l2 = l[n // 2:]
        l1 = self.mergesort(l1)
        l2 = self.mergesort(l2)
        res = []
        i1 = 0
        i2 = 0
        while len(res) < n:
            if l1[i1] < l2[i2]:
                res.append(l1[i1])
                i1+=1
                if i1 == len(l1):
                    res += l2[i2:]
                    break
            else:
                res.append(l2[i2])
                i2+=1
                if i2 == len(l2):
                    res += l1[i1:]
                    break
        return  res


class Squidward:
    def __init__(self, dna):
        self.dna = self.encode(dna)

    def encode(self, dna):
        for i in range(len(dna)):
            if dna[i] == 'x':
                dna += str(i)
                return  dna

    def transcode(self):
        res = ''
        i = 0
        while i < len(self.dna) - 2:
            if self.dna[i] == self.dna[i+1] and self.dna[i] == self.dna[i+2]:
                res += '(0_0)'
                i += 3
            else:
                res += self.dna[i]
                i += 1
        res += self.dna[i:]
        return res


def parser(dna):
    if dna[0] == 'm':
        return Crab(dna)
    elif dna[0] == 's':
        if dna[1] == 'b':
            return SpongeBob(dna)
        return Squidward(dna)

s = input()
cls = parser(s)
if cls == None:
    cls = parser(s[::-1])
if cls == None:
    print("invalid input")
else:
    print(cls.transcode())