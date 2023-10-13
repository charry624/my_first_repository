
"""
#파일 생성 
#f = open("new.txt", 'w')
f = open("temp.txt",'w+')
f.close()


#파일쓰기 
file = open("temp.txt", "w")
#file.write("hello/n")
file.write("hello")
file.write("world")
file.close()


file = open("temp.txt", "w")

for i in range(100):
    file.write(f"{i}\n")

file.close()


#c:/User/Catholic/temp.txt

f=open("c:\\Users\\Catholic\\abcd\\my_first_repository\\temp.txt","w")
f.write("hello")
f.write("world")
f.close()

#파일 읽기 

f = open("temp.txt", "r")
res = f.read()
print(res)

f.close()

#다른 경로로 파일 읽기 
f = open("c:\\Users\\Catholic\\abcd\\my_first_repository\\temp.txt", "r")
res = f.read()
print(res)

f.close()


#readline 

#f = open("temp.txt", "r")
f = open("temp.txt","r")

res = f.readline()
print(res)

f.close()



#readlines 읽기 

f = open("temp.txt","r")
res = f.readlines()
print(res)

f.close()

#readlines 읽기 

f = open("temp.txt","r")
line = f.readlines()
for l in line:
    print(1)

f.close()
"""

#file object 

f = open("temp.txt","r")
for line in f :
    print(line)

f.close()
