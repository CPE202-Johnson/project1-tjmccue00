# int -> T/F
#Function that sees if a given integer can win the bear game
def bears(n):
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
            b = bears(n/2)
            if b == True:
                return(True)
        if n % 3 or n % 4 == 0:
            bers = n - int(str(n)[len(str(n))-2:-1])*int(float(str(n)[-1]))
            if bers > 0:
                a = bears(bers)
                if a == True:
                    return(True)
