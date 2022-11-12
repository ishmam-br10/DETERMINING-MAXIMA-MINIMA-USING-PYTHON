from sympy import *
import sympy as smp
x = symbols('x')
f = smp.sin(x)
# DIFFERENTIATE IT TWO TIMES
diff1 = diff(f,x,1)
diff2 = diff(f,x,2)
subs1 = diff2.subs(x,-5)
subs2 =diff2.subs(x, 6)
if subs1 > 0:
    print(f'Minima : -5')
    print(f'Maxima: 6')
else:
    print(f'Maxima: -5')
    print(f'Minima: 6')
