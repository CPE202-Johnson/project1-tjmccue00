# int -> str
#Recursive function that returns a string representing num in the base b
def convert(num, b):
    num = int(num)
    b = int(b)
    if num == 0:
        return "0"
    n = num // b
    r = num % b
    l = convert(n, b)
    if r == 10:
        r = 'A'
    if r == 11:
        r = 'B'
    if r == 12:
        r = 'C'
    if r == 13:
        r = 'D'
    if r == 14:
        r = 'E'
    if r == 15:
        r = 'F'
    if '0' == str(l):
        return str(r)
    else:
        new = str(l) + str(r)
    return(new)
