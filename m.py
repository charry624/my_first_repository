
#집합 
my_set = {1,2,3,4,5}
setItem = {5,3,1}
print(my_set)
print(setItem)
#집합활용
my_set = {5,8,3,7,1,"h"}
print(my_set)
print(*my_set)
#생성 
my_set =set([5,8,3,7,1,"h"])
print(my_set)
set_tmp =set("hello")
print(set_tmp)
#합집합 
my_set = {5,8,3,7,1,"h"}
set_item = {7,8,4,2,"h"}
print(my_set|set_item)
#print(my_set.union(set_item))
#차집합
#print(my_set - set_item)
print(my_set.difference(set_item))
#교집합
#print(my_set & set_item)
print(my_set.intersection(set_item))
#추가
print(my_set)
my_set.add(9)
print(my_set)
my_set.update([5,9,7,4])
print(my_set)
#삭제
my_set.remove(5)
my_set.discard(2)
print(my_set)
#공통된 요소 삭제 
my_set =set([5,8,3,7,1,"h"])
set_item = {7,8,4,2,"h"}
print(my_set)
my_set.difference_update(set_item)
print(my_set)
#타입변환
my_int = 10 
my_str = str(my_int)
print(my_int)
print(my_str)
print(my_int+10)
my_str = str(my_int)
print(my_str + "hello")
#변환확인 
my_str = '10'
print(my_str)
my_int = int(my_str)
print(my_int)
print(my_int + 10)
#my_int2 = int("ten")
#print(my_int2)

#산술연산자
a=10
b=3 

c=a+b
c=a-b
c=a*b
c=a/b
c=a%b
c=a//b
print(a**b)
print(c)
#할당연산자와 연산자축약
a=2
print(a)
a+=2
print(a)
a-=1
print(a)
a*=4
print(a)
a/=2
print(a)
a**=3
print(a)
#비교, 관계 연산자 
a=10
b=4
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b) #양쪽식이 같지 않다는 의미 
#논리 연산자 
a=1
b=0
print(a and b)
print(a or b)
print(not a)
print(not b)

x=True
y=False

print(x and y)
print(x or b)
print(not x)
print(not y)

# 비트 연산자 
a=10
b=3
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a<<b)
print(a>>b)
#멤버 연산자 
my_list=[9,4,3,7,8,'hi']
print(4 in my_list)
print(2 in my_list)
print(2 not in my_list)
my_dic = {"key1" : "v1", "k2" : "v2"}
print("k2" in my_dic)
