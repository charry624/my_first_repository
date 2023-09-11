#변수참조
my_var = 10
print(my_var)
my_list = [1,2,3]
print(*my_list)
#숫자
#정수
my_int = 10 
#부동 소수점 
my_float = 3.14
#복소수 
my_complex = 3 + 4j
print(my_int)
print(my_float)
print (my_complex)
#문자
my_character = 'A'
my_char = "@"
#문자열
my_string = 'Hello, World'
str_name = "python"
print(my_character)
print(my_char)
print(my_string)
print(str_name)
#불리언
my_bool = True 
bFlag = False 
print(my_bool)
print(bFlag)
#리스트
my_list = [1,2,'three',True]
lsElement = [3.14, "b", "two", False]
print(my_list)
print(lsElement)
#리스트활용
my_list = [10,3,8,9,42,"hello"] 
print(my_list)
print(*my_list)
my_list = [10,3,8,9,42,8,"hello"]
print(my_list)
#크기확인
print(my_list.__len__())
#인덱스
my_list = [10,3,8,9,42, "hello"]
print(my_list)
print(my_list[3])
list_el = my_list[2]
print(list_el)
#엘레멘트 변경 
print(my_list) 
my_list[3] = 11
print(my_list)
n_add = my_list[3] + my_list[2]
print(n_add)
#슬라이싱
print(my_list[2:5])
print(my_list[:3])
print(my_list[4:])
#이중리스트
my_list = [10,3,8,9,42,"hello", [5,4,2, "world"]]
print(my_list)
print(my_list[6][1])
print(my_list)
print(my_list[6][2:])
print(my_list[5][2])
#메소드
my_list = [10,3,8,9,42,8,"hello"]
print(my_list)
my_list.insert(2,4)
print(*my_list)
print(my_list.index(3)) 
print(my_list.index(4)) #오류발생 4 is not in list 

print(my_list)
my_list.append(22)
print(*my_list)
print(my_list.count(8))
print(my_list.count(5))

print(my_list)
print(my_list.pop())
print(*my_list)

my_list =['a', 'b', 'c']
print(my_list)
my_list.sort()
print(*my_list) 
my_list.reverse()
print(*my_list)

list_tmp = [5,7,"world"]

print(my_list, list_tmp)
my_list.extend(list_tmp)
print(*my_list)

print(my_list, list_tmp)
my_list.extend(list_tmp)
print(*my_list)
list_tmp.clear()
print(list_tmp)

my_list = [10,3,8,9,42,8,"hello"]
print(my_list)
my_list.remove(3)
print(*my_list)
print(my_list)
del my_list[2]
print(*my_list)
#튜플
my_tuple = (1,2,'three', True)
tpItem = (3.14, "b", 'two', False)
print(my_tuple)
print(tpItem)
my_tup = (4,2,6,1,"py","w")
print(my_tup)
#크기
print(my_tup.__len__())
#인덱스
print(my_tup)
print(my_tup[2])
print(*my_tup)
print(my_tup)
print(my_tup[2])
# my_tup[3] = 2
print(*my_tup)

my_tup = (4,2,6,1,"py","w")
print(my_tup)
print(my_tup[2] + my_tup[0])
print(*my_tup) 
print(my_tup)
n_add = my_tup[1] + my_tup[3]
print(n_add)
#슬라이싱 
print(my_tup[2:5])
print(my_tup[1:4])
print(my_tup[:3])
print(my_tup[:2])
#이중튜플 
my_tup = (4, 2, 6, 1, "py", "w", ("h", 8, 7, 3))
print(my_tup)
print(my_tup[6][0])
#메소드
my_tup = (4,2,6,1,"py","w")
print(my_tup.index(2,0,3))
print(my_tup.index("py",3,5))
#print(my_tup.index(1,0,3)) - 오류발생
#딕셔너리 
my_dict = {'key1': 'value1', 'key2': 'value2'}
dicData = {"name" : "python", "number" : 23564897}
print(my_dict)
print(dicData)
#출력
my_item = my_dict.items()
print(my_item)
#생성
idx = ("key", "key2", "key3")
dicts = dict.fromkeys(idx,"0")
print(dicts)
#인덱싱
print(my_dict["key1"])
my_str = my_dict.get("key2")
print(my_str) 
print(my_dict.pop("key1"))
print(my_dict)
#복사
dicts = my_dict.copy()
print(dicts)
print(my_dict)
#추가/변경 
my_dict["key3"] = "value3"
print(my_dict)
my_dict.setdefault("key3")
print(my_dict)
my_dict.update({"key1" : "v4"})
print(my_dict)
#삭제 
del my_dict["key2"]
print(my_dict)
#검색 
print("key2" in my_dict)
print("key3" in my_dict)
#변환 
my_list = list(my_dict.keys())
print(my_list)
my_set = set(my_dict.keys())
print(my_set)
#삭제 
my_dict.clear()
print(my_dict)
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







