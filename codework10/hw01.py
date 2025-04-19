def average(nums):
    return sum(nums) / len(nums)

def count(nums):
    days = 0
    for num in nums:
        if num >= 5:
           days += 1
    return days

def get_rain_events(rainfalls):
    events = []
    c_days = 0 # 계속 비온 날짜 
    for rain in rainfalls:
        if rain > 0:
            c_days+=1
        else:
            if c_days > 0:
                events.append(c_days)
            c_days = 0
    if c_days > 0: # 마지막에 비가 멈추지 않으면 마지막 연속강우일 수가 삭제됨
        events.append(c_days) # 고로 여기서, 저장해줌.
    # print(events)
    return events

def rain_event(rainfalls):
    events = []
    rain_days = 0 # 계속 비온 날짜 
    for rain in rainfalls:
        if rain > 0:
            rain_days+=rain
        else:
            if rain_days > 0:
                events.append(rain_days)
            rain_days = 0
    if rain_days > 0: # 마지막에 비가 멈추지 않으면 마지막 연속강우일 수가 삭제됨
        events.append(rain_days) # 고로 여기서, 저장해줌.
    # print(events)
    return events

def sumifs(rainfalls, months, selected=[6,7,8]):
    total = 0
    # for rain in rainfalls: 와 밑은 같다 
    for i in range(len(rainfalls)): # 사실상.. days네 날들 1일 2일 3일 4일
        rain = rainfalls[i] # i가 2면, 2일날의 강우량
        month = months[i] # i가 2면, 2일날의 달 > 1월이겠지. 
        if month in selected: # month가 selected안에 들어갔다면면
            total += rain # total에 rain을 더해라
    return total

def get_weather_db(filename, n): #col_idx == n 콜룸인덱스는 교수님이 쓴 매개변수
    weather_datas = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",")
            #print(tokens[n, type(tokens[n])])
            weather_datas.append(float(tokens[n]))

    return weather_datas

def get_weather_db2(filename, n): #col_idx == n 콜룸인덱스는 교수님이 쓰신 매개변수
    weather_datas = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",") # 가져온줄 리스트화 [10도, 200mm, 2021년]
            #print(tokens[n, type(tokens[n])])
            weather_datas.append(int(tokens[n]))

    return weather_datas


def main():
    filename = "codework10/weather(146)_2022-2022.csv"
    # 1. 일평균 기온의 연평균
    tavgs = get_weather_db(filename, 4)
    rainfive = get_weather_db(filename, 9)


    # print(f"일평균 기온은 {average(tavgs):.2f}도")
    # print(f"5mm이상의 강우일수는 {count(rainfive)}일입니다.")
    # print(f"{sum(rainfive):.2f}")

    # 4 최장연속강우일수
    print(f"최장연속강우일수는 {max(get_rain_events(rainfive))}일입니다.")
    # 5 강우이벤트 중 최대 강수량은? 비가 연속으로 올 때, 하나의 강우 이벤트로 가정
    print(f"강우 이벤트 중 최대 강수량은 {max(rain_event(rainfive)):.2f}mm입니다.")

    # 6 top 3 of tmax
    top3_tmax = sorted(get_weather_db(filename, 3))[-3:]
    print(f"가장 높은 최고기온 3개는 {top3_tmax}입니다.")

    # 여름철 6-8월 총 강수량  
    # rainfalls = 읽음
    months = get_weather_db2(filename, 1)
    print(f"여름철 강수량은 {sumifs(rainfive, months, selected=[6,7,8]):.0f}mm입니다.")

    # 2021년 2022년 강수량 구하기 
    filename2 = "codework10/weather(146)_2001-2022.csv"
    years = get_weather_db2(filename2, 0)
    rainfalls = get_weather_db(filename2, 9)
    print(f"2021년 중 강수량은 {sumifs(rainfalls, years, selected=[2021]):.2f}mm입니다.")
    print(f"2022년 중 강수량은 {sumifs(rainfalls, years, selected=[2022]):.2f}mm입니다.")

if __name__ == "__main__":
    main()