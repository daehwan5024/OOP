from sympy import *
x, t, z, nu = symbols('x t z nu')
init_printing(use_unicode=True)
print(integrate(exp(x)*sin(x) + exp(x)*cos(x), x))
