#식별연산
x = [1,2,3]
y = [1,2,3]
z = x

print(x is y)
print(x is z)
print(x is not y)

#조건문 
x = 10
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

#반복문 
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
#이중 FOR문 출력 
my_list = [[1,2,3], [4,5,6], [7,8,9]]

for row in my_list:
    for num in row:
        print(num)
        
for i in my_list:
    print(i)
    
for my_list in sorted(my_list, reverse=True):
    print(my_list)
    
for i in (1,10):
    for j in range(1, 10):
        print(i,"x",j,"=",i*j)
    
    #for ~ else 문 
    rang = [5,8,3,1,6]
    for i in rang:
        print("element:",i)
    else :
        print("end process")
        
        #반복문 제어 
        for i in range(10):
            if i == 7: 
                break 
            elif i ==1:
                continue
            else:
                print("pass", i)
                pass
            print(i)
            
            #while문 
            i = 1
            while i <= 5:
                print(i)
                i+=1
            # 0부터 9까지 출력 
            i =0
            while i <= 9:
                print(i)
                i+=1
            #문자열을 한글자씩 출력 
            str_word = "python"
            idx = 0
            
            while idx < len(str_word):
               print(str_word[idx])
               idx += 1
         # while 1~10 총합 
         
        sum = 0 
        i = 1
         
        while i <= 10:
             sum += i
             i += 1
             
             print(sum)
             
              # 1에서 100까지의 짝수, 홀수 출력하기 
             i=1
             
             while i <= 100:
                if i % 2 == 0:
                     print("짝수 : ", i)
                elif i % 2 == 1:
                    print("홀수 :", i)
                i += 1
            
              # 1에서 100까지의 7의 배수만 출력하기 
        i = 1
            
        while i <= 100 :
            if i % 7 == 0:
                print(i)
            i += 1 
            
            for i in range(10):
                if i == 7:
                    break 
                elif i == 1:
                     continue 
                else: 
                    pass
                
                
              
              