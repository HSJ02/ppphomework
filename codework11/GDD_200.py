def get_weather_data(fname, n):
    weather_dates = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_dates.append(float(tokens[n]))
    return weather_dates 

def get_weather_dates(fname):
    weather_dates = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_dates.append([int(tokens[0]), int(tokens[1]), int(tokens[2])])
    return weather_dates 

def gdd_season(tavg, dates, selected):
    temp_cum = 0
    base_temp = 5
    for i in range(len(tavg)):
        t = tavg[i]
        if dates[i][0] in [selected]:
            if dates[i][1] in [4, 5, 6, 7, 8, 9]:
                if t >= base_temp:
                    temp_cum += (t-base_temp)
                    if temp_cum >= 200:
                        
                        return dates[i]


def main():
    filename = "codework11/weather(146)_2001-2022.csv"
    dates = get_weather_dates(filename)
    tavg = get_weather_data(filename, 4)
    year = 2000
    for i in range(1,23):
        year += 1
        print(f"{year}년에 GDD가 200°C-day을 최초로 넘는 날짜는 {gdd_season(tavg, dates, year)}입니다.")

if __name__ == "__main__":
    main()