import matplotlib.pyplot as plt



#기본사용 y 
#value = [1, 2, 3, 4]
#value = [2,4,5,7,10]
#res = plt.plot(value)
#plt.show()

#두축 설정하기 
#x_value = [2, 3, 6, 7, 10 ]
#y_value = [1, 4, 5, 8, 9]

#plt.plot(x_value, y_value)
#plt.plot([2,3,6,7,10], [1,4,5,8,9])
#plt.show()

#딕셔너리 설정 

#dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

#plt.plot("x_data", "y_data", data=dic_val)
#plt.show()

#레이블 설정 

#dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

#plt.plot("x_data", "y_data", data=dic_val)

#plt.xlabel("ttttttt")
#plt.xlabel("x_data")
#plt.ylabel("y_data")
#plt.show()

#plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "--", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ":", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "-.", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ".", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ".-", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ".--", label="PData(km)")

#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="solid", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashed", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dotted", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashdot", label="PData(km)")

#solid 픽셀크기 - 간격 
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0,(1,0)), label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0,(4,0)), label="PData(km)")

#스타일
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="b", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="red", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="#02BA53", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C1", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C6", label="Value(m)")

#두께

#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10,color = "C6", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=10,color = "C6", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, solid_capstyle="round", color = "C6", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, solid_capstyle="butt", color = "C6", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=10, solid_capstyle="round", color = "C6", label="Value(m)"

#마커지정 
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "cd", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo", label="PData(km)")

#plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo-", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo--", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo-.", label="PData(km)")

#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="H", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="D", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="x", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker=11, label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="s", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="$test$", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="$y$", label="PData(km)")

#그래프 영역 채우기 
xdata = [2,3,6,7,10]
ydata = [1,4,5,8,9]
y1data = [2,4,6,8,10]

plt.plot(xdata,ydata)
plt.xlabel("x_data")
plt.ylabel("y_data")

#세로 축 채우기
#plt.fill_between(xdata[1:4], ydata[1:4], alpha=0.5)
#plt.fill_between(xdata[2:4], ydata[2:4], alpha=0.5)
#plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.5)
#plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.3)

#가로 축 채우기
#plt.fill_betweenx(ydata[1:3], xdata[1:3], alpha=0.3)
#plt.fill_betweenx(ydata[2:4], xdata[2:4], alpha=0.3)

#plt.plot([1,3,5,7,9],[2,4,6,8,10])
plt.plot(xdata,ydata)

#두 선간 채우기
plt.fill_between(xdata[1:4], ydata[1:4], y1data[1:4], alpha=0.5)
#plt.fill_between(xdata[1:3], ydata[1:3], y1data[1:3], alpha=0.5)
#plt.fill_between(xdata[1:3], ydata[1:3], y1data[1:3],color = "C6", alpha=0.5)

#영역 채우기 
#plt.fill([2.9, 2.9, 7.1, 7.1], [2.5, 5.0, 8.5, 6.0], alpha=0.5)
plt.fill([1.9, 1.9, 3.1, 3.1], [0.5, 2.5, 5.5, 4.1], alpha=0.5)

plt.show()

#================================================================

dic_val = {"x_data":[2,3,6,7,10], "y_data":[1,4,5,8,9]}
dic1_val = {"x1_data":[2,3,6,7,10], "y1_data":[1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.plot("x1_data", "y1_data", data=dic_val, label="Value(m)")
#plt.plot([1,4,5,9],[[2,3,8,10]])
plt.xlabel("x-data")
plt.ylabel("y-data")

#배경 그리드
#plt.grid()

#plt.grid(axis="x")

#plt.grid(axis="y")
#plt.grid(color="g", alpha=0.5, linestyle="-")
#plt.grid(axis="x", color="g", alpha=0.5, linestyle="-")
#plt.grid(axis="y", color="r", alpha=0.5, linestyle="-")

#눈금표시
#plt.xticks()
#plt.yticks()

#plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
#plt.yticks([0,1,2,3,4,5,6,7,8,9,10])

#plt.xticks([1,3,5,7,9,11])
#plt.yticks([2,4,6,8,10,12])

# 라벨 지정
#plt.xticks([1,2,3,4,5,6,7,8,9,10], labels=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])
#plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11], labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

plt.tick_params(axis="x", direction="in")
#plt.tick_params(axis="x", direction="out")
plt.tick_params(axis="y", direction="in")

x_years = ['2020', '2021', '2022']
y_data = [100, 400, 900]
clr = ["C2", "lime", "#02BA53"]

#plt.bar(x_years, y_data)

#색 지정
#plt.bar(x_years, y_data, color="g")
#plt.bar(x_years, y_data, color="C7")
#plt.bar(x_years, y_data, color="#02BA53")

#개별 색 지정
#plt.bar(x_years, y_data, color=clr)

#너비설정 
#plt.bar(x_years, y_data, color=clr, width=2)
#plt.bar(x_years, y_data, color=clr, width=0.5)
#plt.bar(x_years, y_data, color=clr, width=0.1)

#위치 선정
#plt.bar(x_years, y_data, color=clr, align="edge", width=0.5)
#plt.bar(x_years, y_data, color=clr, align="center", width=0.3)

#테두리 설정 
#plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", width=0.5)
#plt.bar(x_years, y_data, color=clr, align="center", edgecolor="C3", width=0.5)

#plt.bar(x_years, y_data, color=clr, align="center", edgecolor="blue", linewidth=3, width=0.5)

#축 설정 
#plt.xticks(x_years)
#plt.yticks(y_data,y_data)
#plt.yticks(100,200,300,400,500)

#수평/가로 그래프
plt.barh(x_years, y_data)

#옵션 나열 
plt.barh(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, height=0.3)