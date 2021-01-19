# int -> str
#Recursive function that returns a string representing num in the base b
def convert(num, b):
    if num == 0:
        return ""
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
    new = str(l) + str(r)
    return(new)
