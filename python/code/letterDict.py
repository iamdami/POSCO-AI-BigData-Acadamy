dic = dict()

def letterDict(s):
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
        return dic

def maxLetter(dic):
    new = sorted(dic.items(), reverse=True, key = lambda dic : dic[1])
    return new[0][0]

def comb_dict(d1, d2):
    d1.update(d2)
    return d1

sen = letterDict("you look cute")
# c = comb_dict(a, b)
# print(c)
# print(maxLetter(c))
