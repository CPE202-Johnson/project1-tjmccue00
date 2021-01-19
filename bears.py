# int -> T/F
#Function that sees if a given integer can win the bear game
def bears(n):
    print(n)
    if n < 42:
        print('failed')
        return(False)
    if n == 42:
        return(True)
    if n > 42:
        if n % 5 == 0:
            print('c')
            c = bears(n - 42)
            if c == True:
                return(True)
            else:
                return(False)
        if n % 2 == 0:
            print('b')
            b = bears(n//2)
            if b == True:
                return(True)
            else:
                return(False)
        if n % 3 or n % 4 == 0:
            print('a')
            if '0' not in str(n):
                a = bears(n - int(float(str(n)[len(str(n))-2:-1]))*int(str(n)[-1]))
                if a == True:
                    return(True)
            else:
                return(False)
