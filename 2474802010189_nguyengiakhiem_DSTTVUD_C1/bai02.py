from sympy import solve, Symbol
x = Symbol('x')
ptb2 = x**2 + 9*x + 8
print(solve(ptb2, dict = True))
#[{x: -8}, {x: -1}]
ptb2 = x**2 + 1*x + 10
nghiemx = solve(ptb2, dict = True)
print(nghiemx)
#[{x: -1/2 - sqrt(39)*I/2}, {x: -1/2 + sqrt(39)*I/2}]