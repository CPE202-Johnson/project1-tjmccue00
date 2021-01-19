# str -> list
#This function will take a string and return a list of permutations of the str
def perm_gen_lex(a):
    print(a)
    if len(a) <= 1:
        return [a]
    list = []
    for i in range(len(a)):
        for j in perm_gen_lex(a[:i]+a[i+1:]):
            list += [a[i] + j]
    return list
