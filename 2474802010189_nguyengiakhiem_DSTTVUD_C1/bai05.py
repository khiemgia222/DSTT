import numpy as np 
M1 = np.array([ [9, 12], [23,30] ])
print(M1)
#[[ 9 12]
#[23 30]]
u  = np.array([2,1])
tichM1u = M1.dot(u)
print(tichM1u)
#[30 76]
tichuM1 = u.dot(M1)
print(tichuM1)
#[41 54]
print(np.dot(M1,u))
#[30 76]
print(np.dot(u,M1))
#[41 54]
mat1 = np.zeros([5,5])
print(mat1)
#[[0. 0. 0. 0. 0.]
 #[0. 0. 0. 0. 0.]
 #[0. 0. 0. 0. 0.]
 #[0. 0. 0. 0. 0.]
 #[0. 0. 0. 0. 0.]]
mat2 = np.ones([5,5])
print(mat2)
#[[1. 1. 1. 1. 1.]
 #[1. 1. 1. 1. 1.]
 #[1. 1. 1. 1. 1.]
 #[1. 1. 1. 1. 1.]
 #[1. 1. 1. 1. 1.]]
mat3 = mat1 +2*mat2 
print(mat3)
#[[2. 2. 2. 2. 2.]
 #[2. 2. 2. 2. 2.]
 #[2. 2. 2. 2. 2.]
 #[2. 2. 2. 2. 2.]
 #[2. 2. 2. 2. 2.]]
mat4 = mat3 
print(mat4)
#[[2. 2. 2. 2. 2.]
 #[2. 2. 2. 2. 2.]
 #[2. 2. 2. 2. 2.]
 #[2. 2. 2. 2. 2.]
 #[2. 2. 2. 2. 2.]]
mat3[3][2] = 10 
print(mat4) 
#[[ 2.  2.  2.  2.  2.]
 #[ 2.  2.  2.  2.  2.]
 #[ 2.  2.  2.  2.  2.]
 #[ 2.  2. 10.  2.  2.]
 #[ 2.  2.  2.  2.  2.]]
mat5 = np.copy(mat3)
mat3[3][2] = 10
print(mat5)
mat6 = np.empty([4,5])
print(mat6)
mat7 = np.identity(4)
mat8 = np.random.random([4,5])
print(mat8)