#콜백 함수 

#def prt_func() :
    #print("hello")
    
#def callfunc(fx) :
    #fx()
    
#callfunc(prt_func)

def prt_func(n):
    print("hello",n)
    
def callfunc(fx) :
    for i in range(5) :
        fx(i)
        
callfunc(prt_func)

#타입힌트 - 콜백함수 

def update_msg(name:str) -> list:
    msg = []
    msg.append("Hello," + name)
    msg.append("Bye,"+ name)
    return msg
def greeting(in_name: str) -> list:
    gt_msg = None 
    gt_msg = update_msg(in_name)
    return gt_msg
res = greeting("python")

for message in res: 
    print(message)
    
def ploop(n) :
    if n == 0:
       print("end")
       return 1
    else : 
       print(n, n-1, "=", n+n-1)
       return n * ploop(n-1)
   
print(ploop(3))

pi = 3.14159

def add(x, y):
    return x + y

def cc_len(x) : 
    return x*2*pi

def cc_area(x) : 
    return x * x * pi 

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

#문자열 자르기 

def cutstr(st,wd,idx):
    tmp = st.split(wd)
    res = tmp[idx]
    return res 

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
rs = cutstr(url,"/",4) 
print(rs)

import math 

sq_res = math.sqrt(6)
print(sq_res)

sp_res = math.sin(math.pi/2)
print(sp_res)

e_res = math.log(math.e)
print(e_res)

exp_res = math.exp(3)
print(exp_res)

pi_res = math.pi 
print(pi_res)

fc_res = math.factorial(4)
print(fc_res)

import mod.utils as mu 

res = mu.mt_sqrt(7)
print(res)

sin = mu.mt_sinpi()
print(sin)

el = mu.mt_elog() 
print(el)

ep = mu.mt_exp(3)
print(ep)

pi = mu.mt_pi()
print(pi)

import random as rd

res = rd.randint(1,100)
print(res)

my_list =["apple", "banana","cherry"]
lres =rd.choice(my_list)
print(lres)

fres = rd.random() 
print(fres)

nvres = rd.normalvariate()
print(nvres)