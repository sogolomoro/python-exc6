import re
def rmperspecchar(text, perspeccharpattern):
    fixedtxt = perspeccharpattern.sub('', text)
    return fixedtxt
def similarwords(n, input1, input2, perspeccharpattern):
    input1 = rmperspecchar(input1, perspeccharpattern)
    words = input1.split(" ")
    result = []
    for word in words:
        distance_value = distance(word, input2)  
        if distance_value <= n:
            result.append(word)
    return result
def distance(word1, word2):
    len1, len2 = len(word1), len(word2)
    if len1 < len2:
        word1 += '_' * (len2 - len1)
    elif len1 > len2:
        word2 += '_' * (len1 - len2)
    distance_value = sum(c1 != c2 for c1, c2 in zip(word1, word2))
    return distance_value
perspeccharpattern = re.compile(r'[،]+')
n = int(input())
input1 = input()
input2 = input()
result = similarwords(n, input1, input2, perspeccharpattern)
for word in result:
    print(word)