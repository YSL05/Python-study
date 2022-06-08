def gcd(x = 0,y = 0):
    """gcd"""
    if x > y:
        (x,y) = (y,x) 
    for factor in range(x,0,-1):
        if x % factor == 0 and y % factor == 0:
            return factor

def icm (x,y):
    """icm"""
    return x * y // gcd(x,y)

print(gcd(6,8))
print(icm(6,8))