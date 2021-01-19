# int -> T/F
#Function that sees if a given integer can win the bear game
def bears(n):
    a = 0
    b = 0
    c = 0
    if n < 42:
        return(False)
    if n == 42:
        return(True)
    if n > 42:
        if n % 5 == 0:
            c = bears(n - 42)
            if c == True:
                return(True)
        if n % 2 == 0:
            b = bears(n//2)
            if b == True:
                return(True)
        if n % 3 or n % 4 == 0:
            if '0' not in str(n):
                a = bears(n - int(float(str(n)[len(str(n))-2:-1]))*int(str(n)[-1]))
                if a == True:
                    return(True)
    if a or b or c == False:
        return False

print(bears(72))
