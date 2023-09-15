#식별연산
x = [1,2,3]
y = [1,2,3]
z = x

print(x is y)
print(x is z)
print(x is not y)

#식별 
a = 5
b = 5
print(a is b)
print(a is not b)

3 == 3.0
3 is 5.0
 
#특성 
a = [3,5,1]
b=a
a[0] = 2

print(a,b)
print(a is b)

#연산자 결합 순서 
x = 2**3**2 
print(x)

#a=2+3*4
#a=10/5/2
#a=2**3**2 
#a=2**(3**2)
#a=10%3%2
#a=1+2>3 and 4-1<2
#a = not False and True 
#a = not True or False and True 
#a = 1 & 2 | 3 ^ 4
#a = 5 in [3,4,5] or 2 not in [1,2,3]
#a = 2*-3//2
#a = 1==2 !=3
print(a)