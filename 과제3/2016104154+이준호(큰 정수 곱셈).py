import math
def digit_length(n):
    return int(math.log10(n)) + 1 if n else 0

def prod2(a,b):
    u = digit_length(a)
    v = digit_length(b)
    n = max(u,v)
    if(a == 0 or b == 0):
        return 0
    elif(n<= 4):
        return a*b
    else:
        m = math.floor(n/2)
        x = a/pow(10,m)
        y = a%pow(10,m)
        w = b/pow(10,m)
        z = b%pow(10,m)
        r = prod2(x+y,w+z)
        p = prod2(x,w)
        q = prod2(y,z)
        return (p*pow(10,2*m) + (r-p-q)*pow(10,m)+q)

a=1234567812345678
b=2345678923456789
print(prod2(a,b))
print(a*b)