"""
from faker import Faker as fk
import os 

#temp = fk()
temp = fk("ko-KR")
print(temp.name())

folder = "data/"
if not os.path.isdir(folder):
    os.mkdir(folder)
    
with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")
    
with open(folder + "fktemp.csv", "w", newline='', encoding='utf8') as f :
    for i in range(30) :
        f.write(temp.name() + "," + 
            temp.address() + "," + 
            temp.postcode() + "," + 
            temp.company() + "," + 
            temp.job() + "," + 
            temp.phone_number() + "," + 
            temp.email() + "," + 
            temp.user_name() + "," + 
            temp.ipv4_private() + "," + 
            temp.ipv4_public() + "," + 
            temp.catch_phrase() + "," + 
            temp.color_name() + "\n")
        
        import pandas as pd

        folder = "data/"
        target = folder + "fktemp.csv"

        df = pd.read_csv(target)
        
        print(df.name == "김영수")
        print(df.company == "박박정")
        
        temp = df[df.postcode > 70000]
        print(temp)
        
        res = df[df.postcode>70000][["name", "postcode", 'color']]
        print(res)
        print(res.count())
        
        temp = df.postcode.mean()
        temp = df.postcode.sum
        print(temp)
        
        temp=df[df.postcode>df.postcode.meam()][["name","postcode"]]
        temp = df[df.postcode>df.postcode.mean()]
        print(temp)
        
        temp = df.compant.insull()
        for el in temp:
            if el == True : 
                print(el)
                
        temp = df.name.empty
        temp = df[df.company.isnull()]["name","postcode"]
        print(temp)
        
        temp = df[(df.color == "Ivory")]
        temp = df[~(df.color == "Ivory")][["name"]]
        print(temp.count())
        print(temp.color.count())
        print(temp)
        
        temp = df[(df.color == "Ivory") & (df.postcode > 70000)]
        temp = df[(df.color == "Ivory") | (df.postcode > 70000)]
        temp = df[(df.color == "Ivory") | (df.postcode > 70000)][["name"]]
        print(temp)
        
        temp = df.sort_values("postcode")
        temp = df.sort_values("name", ascending = False)
        temp = df.sort_values("name", ascending= False) 
        
        import pandas as pd
        
        col = ['Machine', 'Country', 'Price', 'Brand'] 
        data = [['TV', 'Korea', 1000, 'A']]
        ['TV', 'Korea', 1000, 'B']
        ['TV', 'China', 300, 'C']
        ['TV', 'China', 2000, 'D']
        ['TV', 'China', 3000, 'E']
        ['TV', 'China', 450, 'D']
    df = pd.DataFrame(data=data, columns = col)
    print(df)  
    
    print("\n-----------------\n")    
    print(df.pivot(index='Machine', colums = 'Country', values = 'Price'))
    print(df.pivot(index='Brand',columns ='Machine', values = 'Price'))
    print(df.pivot(index='Country', columns = 'Machine', values = 'Price'))
    print(df.pivot(index='Price', columns = 'Brand', values = 'Machine')) 
    
#rank 매기기 
    
import pandas as pd 
    
folder = "data/"
target = folder+"fktemp.csv"

df = pd.read_csv(target) 
df["aver"] = df.postcode.rank(methond="average") 
print(df[["postcode", "dense"]])

df["first"] = df.postcode.rank(method = "dense")
print(df[["postcode", "first"]])

df["min"] = df.postcode.rank(method = "first")
print(df[["postcode","min"]])  

df["max"] = df.postcode.rank(method="min", ascending=False)
df["max"] = df.postcode.rank(method="max")
print(df[["postcode", "max"]])

print(df[["postcode", "max", "min", "first", "dense", "aver"]])

#전치 컬럼 = 로우변환
print(df.transpose())

#누적 계산 
print(df["postcode".expanding().sum()])
print(df["postcode"].expanding())

#내림차순 기준
print(df.postcode.idxmax(axis=0)) 
print(df.postcode.idxmax(axis=0)) 

#empty 추가   
print(df.empty)
print(df.postcode.empty)

print(df.isin([53770]))
print(df.isin(["김윤하"])) 

print(df.isin([53770, 67238]))

print(df.isin([53770, 67238, "박지유"]))

#기간 계산 

period = pd.period_range(start = "2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq ="30T")
dt = {"col1": [1,2,3,4,5,6], "col2":period}
idx = ["row1","row2","row3","row4","row5","row6"]
pf = pd.DataFrame(data=dt, index=idx)
print(df) 

i = pd.data_range("2023-11-10", periods = 10, freq = "1H")
i = pd.data_range("2023-11-10", period =10, freq="3H")
df = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index = 1)       
print(df)

#특정시간 찾기
print("\n----------------\n")
print(df.at_time("09:00"))
print(df.at_time("03:00"))

#범위 찾기
print("\n-----------------\n")       
print(df.between_time(start_time="12:00", end_time="00:00"))
print(df.between_time(start_time="03:00", end_time="09:00"))

#x일 간격 생성 - 기간별 찾기 
i = pd.data_range("2023-11-10", periods=10, freq="3D")
# i = pd.data_range("2023-11-10", periods=10, freq="5D")
df = pd.DataFrame({'col':[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

print(df.first("5D"))

print(df.first("7D"))

print(df.last("7D"))


import FinanceDataReader as fdr

#ksp = fdr.DataReader("KS11", "2023")
ksp = fdr.DataReader("KS11", "2001")
print(ksp)
print("\n-----------------\n")

#최고
#res = ksp["High"].max()
#print(res)

#res = ksp["High"].idxmax()
#rint(res)

#최저
#res = ksp["Low"].min()
#print(res)

#res = ksp["Volume"].nlargest(n=5)
#res = ksp["Volume"].nlargest(n=10)
#print(res)

#res = ksp["Volume"].nsmallest(n=5)
#res = ksp["Close"].nsmallesr(n=5)
##res = ksp["Close"].nlagest(n=5)
#print(res)

#3000최초일
cond = ksp["Close"] >= 3000
cond = ksp["Close"] >=2000
res = ksp[cond].index[0]
print(res)

res = ksp["Volume"] > ksp["Volume"].shift()
print(res)

ksp["up"] = ksp["Volume"]>ksp["Volume"].shift()
print(ksp)

res=ksp["up"] != ksp["up"].shift().cumsum()
print(res)

ksp["grp"] = (ksp["up"] != ksp["up"].shift()).cumsum()
print(ksp)

res = ksp["up_cnt"].max()
print(res)
"""

import pandas as pd

target = "./data/apt.csv"

df = pd.read_csv(target, encoding="CP949")

df.to_csv("./data/conv_apt.csv", encoding="utf8")

print(df.head)

import pandas as pd

df = pd.read_csv("./data/conv_apt.csv", index_col = 0)

print(df.head())

print("\n-----------------\n")
df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
#print(df)
#print(df.dtypes)

#arr = df.to_numpy()
#print(arr)
#print(arr[2])
#print(len(arr))

#print(df.describe())

print(df.transpose())
print("\n-------------------\n")
print(df.T.head())