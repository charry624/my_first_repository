def add(a, b) :
    print("a+b:",a+b)
    return a+b
def sub(a,b) :
    print("a-b:",a-b)
    return a-b 
def mul(a,b):
    print("a*b:",a*b)
    return a* b 
def div(a,b):
    print("a/b:",a/b)
    return a/b

import mod.calc as cl
res = cl.add(8,4)
print(res)
add_res = cl.add(8,4)
sub_res = cl.sub(8,4)
mul_res = cl.mul(8,4)
div_res = cl.div(8,4)

#circle mod 
import mod.circle_mod as cm 

print(cm.pi)

print(cm.cc_area(4))
print(cm.cc_len(5))

