import requests



def get_weather(city):
    api_key = '<d6119321d6df61e7b744ee34af280934>'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}  # 해당 도시의 날씨 정보를 섭씨로 받아옵니다.
    
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    
    if weather_data['cod'] == 200:
        weather = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        
        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Weather information not available")

# 사용자가 원하는 도시 입력
city_name = input("Enter city name: ")
get_weather(city_name)



# diary_app_with_login.py에 추가하는 함수
def start_diary_app(username):
    while True:
        print("\n1. 일기 쓰기")
        print("2. 일기 읽기")
        print("3. 로그아웃")
        inner_choice = input("작업을 선택하세요: ")

        if inner_choice == "1":
            write_diary(username)
        elif inner_choice == "2":
            read_diary(username)
        elif inner_choice == "3":
            break
        else:
            print("올바른 작업을 선택하세요.")

    
# 파일명: diary_app_with_login.py

# 사용자 정보 저장을 위한 딕셔너리
users = {
    "charry": "0624",
    "paul": "1001"
}

# 로그인 기능
def login():
    while True:
        username = input("사용자 이름을 입력하세요: ")
        password = input("비밀번호를 입력하세요: ")

        if username in users and users[username] == password:
            print("로그인 성공!")
            start_diary_app(username)
            return username
        else:
            print("로그인 실패. 다시 시도해주세요.")
            
def change_password(username):
    new_password = input("새로운 비밀번호를 입력하세요: ")
    users[username] = new_password
    print(f"{username}의 비밀번호가 변경되었습니다.")

# 일기 읽기 기능
def read_diary(username):
    file_name = f"{username}_diary.txt"
    date = input("날짜를 입력하세요 (예: 2023-12-01): ")

    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(f"{username}의 일기 내용:\n{content}")
    except FileNotFoundError:
        print(f"{username}의 일기가 없습니다.")

# 일기 쓰기 기능
def write_diary(username):
    date = input("날짜를 입력하세요 (예: 2023-12-01): ")
    file_name = f"{username}_diary.txt"
    content = input("일기 내용을 입력하세요: ")
    city = input("날씨 정보를 확인할 도시를 입력하세요: ")  # 사용자로부터 도시 입력 받기

    weather_info = get_weather(city)  # 입력된 도시의 날씨 정보 가져오기

    try:
        with open(file_name, "a") as file:  # "w" 대신 "a" 모드를 사용하여 파일 끝에 추가
            file.write(f"날짜: {date}\n")  # 날짜 저장
            file.write(f"{username}의 일기:\n{content}\n")  # 사용자의 일기 내용 저장
            file.write(f"{weather_info}\n\n")  # 날씨 정보 추가
        print(f"{username}의 일기와 날씨 정보가 저장되었습니다.")
    except FileNotFoundError:
        print(f"{file_name} 파일을 찾을 수 없습니다.")



# 메인 함수
def main():
    while True:
        print("\n===== 일기장 애플리케이션 =====")
        print("1. 로그인")
        print("2. 비밀번호 변경")
        print("3. 종료")

        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            username = login()
            if username:
                while True:
                    print("\n1. 일기 쓰기")
                    print("2. 일기 읽기")
                    print("3. 비밀번호 변경")
                    print("4. 로그아웃")
                    inner_choice = input("작업을 선택하세요: ")

                    if inner_choice == "1":
                        write_diary(username)
                    elif inner_choice == "2":
                        read_diary(username)
                    elif inner_choice == "3":
                        change_password(username)
                    elif inner_choice == "4":
                        break
                    else:
                        print("올바른 작업을 선택하세요.")
        elif choice == "2":
            username = input("사용자 이름을 입력하세요: ")
            if username in users:
                new_password = input("새로운 비밀번호를 입력하세요: ")
                users[username] = new_password
                print(f"{username}의 비밀번호가 변경되었습니다.")
            else:
                print("존재하지 않는 사용자입니다.")
        elif choice == "3":
            break
        else:
            print("올바른 메뉴를 선택하세요.")

if __name__ == "__main__":
    main()