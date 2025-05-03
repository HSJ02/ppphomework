def average(nums):
    return sum(nums) / len(nums)

def count(nums):
    days = 0
    for num in nums:
        if num >= 5:
           days += 1
    return days


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

import os
import requests

def download_weather(station_id, year, filename):
    URL= f"https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)

def main():
    filename = "codework12/weather(146)_2020-2020.csv"
    if not os.path.exists(filename):
        download_weather(146, 2020, "codework12/weather(146)_2020-2020.csv")
    # filename = "codework10/weather(146)_2022-2022.csv"
    # 1. 일평균 기온의 연평균
    tavgs = get_weather_db(filename, 4)
    rainfive = get_weather_db(filename, 9)


    print(f"일평균 기온은 {average(tavgs):.2f}도")
    print(f"5mm이상의 강우일수는 {count(rainfive)}일입니다.")
    print(f"총강우량은 {sum(rainfive):.2f}mm입니다.")



if __name__ == "__main__":
    main()