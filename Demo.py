from decimal import Decimal
import numpy as np

# This is input f(x)


def f(x):
    return (x**(23-x*x))**(1/43)


SaiSo = 10**-10
# n = int(input('Input n: '))
n = 4
denta = 1.0
res = 0.0

while (1):
    ans = float((f(n) - f(n-denta))/denta)
    
    print('$', res, '\t', denta, '\t', abs(res - ans))
    
    if abs(res - ans) < SaiSo:
        print(res)
        break
    else:
        res = ans
        denta /= 10

print(50)
