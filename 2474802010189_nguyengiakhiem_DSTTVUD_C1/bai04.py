from sympy import symbols, solve 
x,y = symbols('x,y')
pt1 = 2*x + 3*y -12
pt2 = 3*x - 2*y - 5
print(solve((pt1,pt2), dict = True))
#[{x: 3, y: 2}]
nghiem = solve((pt1,pt2),dict = True)
nghiem = nghiem[0]
print(pt1.subs({x:nghiem[x], y:nghiem[y]}))
#0
print(pt2.subs({x:nghiem[x], y:nghiem[y]})) 
#0
