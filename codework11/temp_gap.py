def maximum_temp_gap(dates, tmax, tmin, selected): # => [2021, 1, 20], 23.1, -2.3

    max_gap_date = dates[0]
    max_gap = tmax[0] - tmin[0]
    
    for i in range(len(dates)):
        date = dates[i]
        tx = tmax[i]
        tm = tmin[i]
        year = date[0]
        gap = tx - tm
        if year in selected:
           
            if max_gap < gap:
              max_gap = gap
              max_gap_date = date

                    
    return [max_gap_date, max_gap]

def get_weather_dates(fname):
    weather_dates = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_dates.append([int(tokens[0]), int(tokens[1]), int(tokens[2])])
    return weather_dates 

def get_weather_data(filename, n):
    data = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",")
            data.append(float(tokens[n]))
    return data

def main():
    filename = "codework11/weather(146)_2001-2022.csv" 
    dates = get_weather_dates(filename)
    tmax = get_weather_data(filename, 3)
    tmin = get_weather_data(filename, 5)
    Years = 2000
    for i in range(1,23):
        Years+=1
        max_gap_date, max_gap = maximum_temp_gap(dates, tmax, tmin, [Years])
        print(f"일교차가 가장 큰 일자는 {max_gap_date}이고, 해당일의 일교차는 {max_gap:.1f}도 입니다.")

        

if __name__ == "__main__":
    main()