from sfarm_hw import submit_to_api
import os
import requests

def sumifs(rainfalls, months, selected):
    total = 0
    for i in range(len(rainfalls)): 
        rain = rainfalls[i] 
        month = months[i] 
        if month in selected: 
            total += rain 
    return total

def tmaxifs(tmax, years, selected):
    tmax_list = []
    for i in range(len(tmax)):
        year = years[i] 
        if year in selected:
            tmax_list.append(tmax[i])
    if tmax_list:
            return max(tmax_list)
    
def max_gap(tmax, tmin):
    gap_list = []
    gap = 0
    for i in range(len(tmax)):
        gap = tmax[i]-tmin[i]
        gap_list.append(float(gap))
    return max(gap_list)
        

def get_weather_db(filename, n): 
    weather_datas = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",")
            #print(tokens[n, type(tokens[n])])
            weather_datas.append(float(tokens[n]))

    return weather_datas

def get_weather_db2(filename, n): 
    weather_datas = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",")
            #print(tokens[n, type(tokens[n])])
            weather_datas.append(int(tokens[n]))

    return weather_datas


def download_weather(station_id, year, filename):
    URL= f"https://api.taegon.kr/stations/119/?sy=2024&ey=2024&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)

def main():
    filename = "codework16/weather(119)_2024-2024.csv"
    if not os.path.exists(filename):
        download_weather(119, 2020, "codework16/weather(119)_2024-2024.csv")
    file_jeonju = "codework16/weather(146)_2001-2022.csv"
    file_jeonju2024 = "codework16/weather(146)_2024-2024.csv"

    rainfall = get_weather_db(file_jeonju, 9)
    year = get_weather_db2(file_jeonju, 0)
    print(f"{sumifs(rainfall, year, selected=[2015]):.0f}")
    problem01 = f"{sumifs(rainfall, year, selected=[2015]):.0f}"

    tmax = get_weather_db(file_jeonju, 3)
    tmax2 = get_weather_db(file_jeonju2024, 3)

    tmin = get_weather_db(file_jeonju2024, 5)
    print(f"{tmaxifs(tmax, year, selected=[2022]):.0f}")
    problem02 = f"{tmaxifs(tmax, year, selected=[2022]):.0f}"
    print(f"{max_gap(tmax2, tmin):.0f}")
    problem03 = f"{max_gap(tmax2, tmin):.0f}"

    suwon_rain = get_weather_db(filename, 9)
    year2 = get_weather_db2(filename, 0)
    total_suwon = f"{int(sumifs(suwon_rain, year2, selected=[2024]))}"
    gap_J2S = int(total_suwon) - int(problem01)
    problem04 = abs(gap_J2S)
    

    name = "황승재"
    affiliation = "스마트팜학과"
    student_id = "202217737"

    answer1 = problem01
    answer2 = problem02
    answer3 = problem03
    answer4 = problem04

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)

if __name__ == "__main__":
    main()

