
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
"""

#c:/User/Catholic/temp.txt

f=open("c:/User/Catholic/temp.txt","w")
for i in range(100):
    f.write(f"{i}\\n")

f.close()
