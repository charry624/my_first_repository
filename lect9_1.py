"""
import getpass
pw = input("Pass :")
#pw = getpass.getpass("Pass : ")
print(pw)

import hashlib
hl = hashlib.sha256()
#target = "hello"
#target = "hi"
#target = "world"
#target = "python"
#target = "media"
#target = "media program"
#target = "1234567890"
target = "to be or not to be, That is a question!"

hl.update(target.encode("utf-8"))
print(hl.hexdigest())
#print(hl.digest())


import Crypto.Hash.keccak as kek
#target = "hello"
#target = "hi"
#target = "world"
#target = "python"
#target = "media"
#target = "media program"
#target = "1234567890"
target = "to be or not to be, That is a question!"

kksh = kek.new(digest_bits=256)
kksh.update(target.encode("utf-8"))

print(kksh.hexdigest())

import getpass 
import hashlib

pw = getpass.getpass("Pass: ")
print(pw)

hl = hashlib.sha256()

hl.update(pw.encode("utf-8"))
print(hl.digest())
print(hl.hexdigest())


import hashlib
import os

def pwInsert():
    if os.path.exists('pw.txt'):
        pw = input('insert pass :')
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        with open('pw.txt', 'r') as fp:
            return hs.hexdigest() == fp.read()
        
    else:
        return True
    
if pwInsert():
    pw = input('new2 pass :')
    with open('pw.txt', 'w') as fp:
        hs = hashlib.sha256()
        hs.update(pw.encode("utf-8"))
        fp.write(hs.hexdigest())
    
else:
    print("not allow password")
    


import platform as pf

pn = pf.uname()
print(pn)

pm = pf.machine()
print(pm)

pp = pf.processor()
print(pp)

ps = pf.system()
print(ps)



import urllib.request as ur

url = 'https://www.google.com'
#url = 'https://www.daum.net/'
#url =  'https://xkcd.com/'

#res = urllib.request.urlopen(url)
res = ur.urlopen(url)

web = res.read()

with open("ul.html", "wb") as fp:
    fp.write(web)
    
#print(web.decode('utf-8))
print(web)



import http.client as hc

#url = 'https://www.google.com'
url = "www.google.com"

#conn = http.client.HTTPSConnection(url)
conn= hc.HTTPSConnection(url)
conn.request("GET", "/")

r = conn.getresponse()

with open("ulrp.html", "wb") as fp:
    fp.write(r.read())
    
    
conn.close()

print(r)



import time 

#싱글스레드

start = time.time()
def counter(str_name):
    for i in range(50000):
         print(f"Countdown {i}, name : {str_name}\n")
         
    for i in range(3) :
        counter(f"num{i}")
        
    end = time.time()
    
    print("single end", end - start)
    
    

# 멀티스레드(동시에 처리를 한다)

import threading as td

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")


thread1 = td.Thread(target=counter, args=("1num",))
thread2 = td.Thread(target=counter, args=("2num", ))
thread3 = td.Thread(target=counter, args=("3num", ))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("multi end")
         


#병렬 처리 

import multiprocessing 
import time

def counter(str_name):
    for i in range(50000):
        print(f"Countdown {i}, name : {str_name}\n")
        
process1 = multiprocessing.Process(target=counter, args=("1num",))
process2 = multiprocessing.Process(target=counter, args=("2num",))
process3 = multiprocessing.Process(target=counter, args=("3num",))

start = time.time()


process1.start()
process2.start()
process3.start()

process1.join()
process2.join()
process3.join()
end = time.time()

print("proc-end", end-start)

"""

#main 실행 

def main() :
    print("hello world")

def run() :
    print("hello python")

if __name__ == "__main__":
    #run()
    main()