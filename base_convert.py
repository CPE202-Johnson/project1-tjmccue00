# int -> str
#Recursive function that returns a string representing num in the base b
def convert(num, b):
    if num == 0:
        return ""
    n = num // b
    r = num % b
    l = convert(n, b)
    new = str(l) + str(r)
    return(new)
