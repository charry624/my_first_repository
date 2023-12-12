"""
#다중 객체를 이용한 막대 그래프 출력

import matplotlib.pyplot as plt

x_years = ["2020", "2021", "2022"]
y_data = [100, 400, 900]

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
# ax1.bar(x_years, y_data)
# ax2.bar(x_years, y_data)
# ax3.bar(x_years, y_data)
# ax4.bar(x_years, y_data)

ax1.bar(x_years, y_data, color="aquamarine", edgecolor="black", hatch="/")
ax2.bar(x_years, y_data, color="salmon", edgecolor="black", hatch="||")
ax3.bar(x_years, y_data, color="navajowhite", edgecolor="black", hatch="+")
ax4.bar(x_years, y_data, color="lightskyblue", edgecolor="black", hatch="*")

plt.tight_layout()

plt.show() 

# seaborn 상관관계

import FinanceDataReader as fdr 
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

# 각 지표별 상관관계

tips = sns.load_dataset("tips")
print(tips)

# sns.regplot(x="total_bill", y="tip", data=tips)

#sns.barplot(x="day", y="tip", data=tips)
# sns.barplot(x="day", y="total_bill", data=tips)
# sns.barplot(x="tip", y="total_bill", data=tips)
# sns.barplot(x="sex", y="total_bill", data=tips)
# sns.barplot(x="sex", y="tip", data=tips)
# sns.barplot(x="smoker", y="total_bill", data=tips)
# sns.barplot(x="smoker", y="tip", data=tips)
# sns.barplot(x="time", y="total_bill", data=tips)
sns.barplot(x="day", y="total_bill", data=tips, palette="viridis")

plt.title("Average Tips")
plt.xlabel("x")
plt.ylabel("Average")

plt.show()

# 타이타닉 데이터

import FinanceDataReader as fdr 
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

titanic = sns.load_dataset("titanic")

sns.barplot(x="sex", y="survived", hue="pclass", data=titanic)

plt.show()

# 탑승클래스별 인원구성
# 클래스별 생존자
# 성별별 생존자
# 싱글 여행자별 인원구성

import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

titanic = sns.load_dataset("titanic")

# sns.countplot(x="class", hue="who", data=titanic)
# sns.countplot(x="class", hue="alive", data=titanic)
# sns.countplot(x="sex", hue="alive", data=titanic)
# sns.countplot(x="alone", hue="who", data=titanic)

# 탑승지별 생존자의 클래스 구별

# sns.barplot(x="embark_town", y="survived", hue="pclass", data=titanic)
sns.barplot(x="sex", y="survived", hue="pclass", data=titanic)

plt.show()



import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 주식 데이터 분석

df = fdr.DataReader("KS11")
df0 = df.loc["2023"]

print(df0)

# df0["Open"].plot()
# df0["High"].plot()
# df0["Low"].plot()
df0["Close"].plot()

plt.grid(True)
plt.show()

import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 다우지수와 코스피 비교

dow = fdr.DataReader("DJI", "2010-06-01")
kospi = fdr.DataReader("KS11", "2010-06-01")

# plt.figure(figsize=(7, 7))

# 각 지수별 종가 기준 그래프 출력

# 종가 기준

# plt.plot(dow.index, dow.Close, "r--", label="Dow")
# plt.plot(kospi.index, kospi.Close, "b", label="KOSPI")

# 최고가 기준

# plt.plot(dow.index, dow.High, "r--", label="Dow")
# plt.plot(kospi.index, kospi.High, "b", label="KOSPI")

# 해당 날짜 기준 증가 상승율, 상대 수익률 계산

d = (dow.Close / dow.Close.loc["2010-06-01"]) * 100
k = (kospi.Close / kospi.Close.loc["2010-06-01"]) * 100
plt.plot(d.index, d, "r--", label="Dow")
plt.plot(k.index, k, "b", label="KOSPI")

plt.grid()

plt.legend()
plt.show()

# 국내 개별 종목 분석

import FinanceDataReader as fdr
import seaborn as sns
import pandas as pd
import requests
from datetime import datetime
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

url = "https://finance.naver.com/item/sise_day.nhn?code=005930"
# url = "https://finance.naver.com/item/sise_day.nhn?code=068270"

res = requests.get(url, headers=headers)
html = bs(res.text, "html.parser")
html_table = html.select("table")
table = pd.read_html(str(html_table))

print(table)

df_list = []

page = 1
for page in range(1, 10):
    page_url = f"{url}&page={page}"
    print(page_url)

    response = requests.get(page_url, headers=headers)
    html = bs(response.text, "html.parser")
    html_table = html.select("table")
    table = pd.read_html(str(html_table))

    if not table[0].empty:
        df_list.append(table[0].dropna())
        page += 1
    else:
        break

print(df_list)

df = pd.concat(df_list, ignore_index=True)

df = df.dropna()
df = df.iloc[0:30]
df = df.sort_values(by="날짜")

plt.figure(figsize=(15, 5))
plt.title("Target (close)")
plt.xticks(rotation=45)
plt.plot(df["날짜"], df["종가"], "co-")
plt.grid(color="gray", linestyle="--")
plt.show() 

# 미국 개별 종목 분석

import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import yfinance as yf

# ticker = "APPL"
ticker = "MSFT"
start_date = "2022-01-01"
end_date = "2023-12-02"

data = yf.download(ticker, start=start_date, end=end_date)

plt.figure(figsize=(12, 6))
plt.plot(data["Close"], label="Close Price")

data["MA_50"] = data["Close"].rolling(window=50).mean()
data["MA_200"] = data["Close"].rolling(window=200).mean()

plt.plot(data["MA_50"], "r")
plt.plot(data["MA_200"], "b")

plt.title("Stock Price")
plt.xlabel("Data")
plt.ylabel("Price($)")
plt.legend()
plt.show() 

# 국가별 인구 데이터 분석

import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/world-population/population-by-country/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

countries = []
populations = []

rows = soup.select("#example2 tbody tr")
for row in rows:
    columns = row.select("td")
    country = columns[1].get_text(strip=True)
    population = int(columns[2].get_text(strip=True).replace(",", ""))
    
    countries.append(country)
    populations.append(population)

# 상위 10개 국가 시각화

top_countries = countries[:10]
top_populations = populations[:10]

plt.figure(figsize=(12, 6))
plt.barh(top_countries[::-1], top_populations[::-1], color="skyblue")
plt.xlabel("Population")
plt.title("Top 10")
plt.show() 

"""