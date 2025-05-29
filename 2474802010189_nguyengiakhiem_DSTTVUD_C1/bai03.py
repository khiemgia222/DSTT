from sympy import symbols, solve 
x, a, b, c = symbols('x,a,b,c')
ptb2 = a*x*x + b*x + c 
nghiem = solve(ptb2, x, dict = True)
print(nghiem)
#[{x: (-b - sqrt(-4*a*c + b**2))/(2*a)}, {x: (-b + sqrt(-4*a*c + b**2))/(2*a)}]