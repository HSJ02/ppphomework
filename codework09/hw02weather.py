# 연 평균 기온(일평균 기온의 연평균), 5mm이상 강우일수,
# 총 강우량을 구하시오.

# 1. 모든 날의 온도 다 더해서 365로 나누면 될 듯 
# 2. if 문으로 5mm이상 강우 찾아서 total +=하자
# 3. 총 강우량은 더하면 된다.

def av_read_db(filename):
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        total_temp = 0
        days = 0
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",") # 토큰은 이제 리스트
            total_temp += float(tokens[4])
            days += 1
        av_temp = total_temp/days

    return av_temp

def rainfive_read_db(filename):
    #9번값 즉 강우량 값이 있을 거야 여기서 5 이상 횟수 더하기기
    days = 0
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",") # 불러온 자료 리스트화 끝
            if float(tokens[9]) >= 5:
                days += 1
    return days 

def raintotal_read_db(filename):
    total = 0
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",") # 불러온 자료 리스트화~
            total += float(tokens[9])
            
    return total

def main():
    infor_2022 = "codework09/weather(146)_2022-2022.csv"
    print(f"2022년의 연평균 기온은 {av_read_db(infor_2022):.2f}℃ 입니다")
    print(f"2022년의 5mm 이상 강우일수는 {rainfive_read_db(infor_2022):.0f}일 입니다")
    print(f"2022년의 총 강우량은 {raintotal_read_db(infor_2022):.2f}mm입니다. ")

if __name__ == "__main__":
    main()