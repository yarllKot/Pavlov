import math
ITTERATIONS=20;
def coss(x):
    x_pow=x
    result=1
    fact=1
    for i in range(1, ITTERATIONS):
        x_pow=(-1)**i*x**(2*i)
        fact*=2*i-1
        fact*=2*i
        result+=x_pow/fact
    return(result)
print(coss(0.4))
print(math.cos(0.4))