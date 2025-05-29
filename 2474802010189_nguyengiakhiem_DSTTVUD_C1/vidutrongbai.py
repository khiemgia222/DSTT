print('vd1:')
ds1 = [1,3]
ds2 = [5,7]
ds = ds1 + ds2 
print(ds)
ds_gapdoi= 2* ds
print(ds_gapdoi)
ds_moi = len(ds)//2
print(ds_moi)
mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"]
thu_tu = [2, 3, 4, 1]
diem_so = [10, 9, 8, 7]
anh_xa = zip(thu_tu, mon_hoc, diem_so)
print(anh_xa)
taphop = set(anh_xa)
print(taphop)
try:
    lay_TT, lay_monhoc, lay_diem = zip(*anh_xa)
    print(lay_monhoc)
except ValueError:
    lay_TT, lay_monhoc, lay_diem = (), (), ()
    print("Không có dữ liệu để trích xuất.")

import itertools
tapsinh = list(itertools.chain(range(4),range(5,10), range(15,20)))
print(tapsinh)
print(list(zip(range(4),range(7,12),reversed(range(11)))))
mylist = [100,200,300]
a,b,c = mylist
print (a,b,c)
print()
print('vd2:')
from sympy import Symbol
x = Symbol('x')
f = x + x + x + 2
print(f)
a = Symbol('Noi')
b = Symbol('Chim')
print(3*b + 7*a)  
a = Symbol('Noi')
b = Symbol('Chim') 
print(a.name)
print(b.name)
from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
s = x*y + y*x
print(s)

p = x*(x+2*x)
print(p)
p = (x+2)*(y+3)
print(p)

p = (x+2)*(y+3) + (x+2)*(x-3)
print(p)
p = x*(-x+2*x-x)
print(p)
p = (x+2)*(y+3)
print(p.expand())
from sympy import factor
bieuthuc = x**3 - y**3
print(factor(bieuthuc))
from sympy import expand
bieuthuc = (x - y)*(x**2 + x*y + y**2)
print(expand(bieuthuc))   
from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y
print(bieuthuc)


