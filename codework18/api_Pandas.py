from sfarm_hw import submit_to_api
import os
import requests
import pandas as pd

def download_weather(station_id, year, filename):
    URL= f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)

def Jeonju(year):
    filename = f"codework18/weather(146)_{year}-{year}.csv"
    df = pd.read_csv(filename, skipinitialspace=True)
    return df


def main():
    filename_jeonju_2012 = "codework18/weather(146)_2012-2012.csv"
    if not os.path.exists(filename_jeonju_2012):
        download_weather(146, 2012, "codework18/weather(146)_2012-2012.csv")
    filename_jeonju_2024 = "codework18/weather(146)_2024-2024.csv"
    if not os.path.exists(filename_jeonju_2024):
        download_weather(146, 2024, "codework18/weather(146)_2024-2024.csv")
    filename_jeonju_2020 = "codework18/weather(146)_2020-2020.csv"
    if not os.path.exists(filename_jeonju_2020):
        download_weather(146, 2020, "codework18/weather(146)_2020-2020.csv")
    filename_jeonju_2019 = "codework18/weather(146)_2019-2019.csv"
    if not os.path.exists(filename_jeonju_2019):
        download_weather(146, 2019, "codework18/weather(146)_2019-2019.csv")

    filename_suwon = "codework18/weather(119)_2019-2019.csv"
    if not os.path.exists(filename_suwon):
        download_weather(119, 2019, "codework18/weather(119)_2019-2019.csv")
    
    
    problem01 = f"{Jeonju(2012)['rainfall'].sum():.1f}"
    problem02 = Jeonju(2024)["tmax"].max()
    problem03 = (Jeonju(2020)["tmax"] - Jeonju(2020)["tmin"]).max()
    df_S = pd.read_csv(filename_suwon, skipinitialspace=True)    
    problem04 = f"{abs(df_S['rainfall'].sum() - Jeonju(2019)['rainfall'].sum()):.1f}"


    print(problem01)
    print(problem02)
    print(problem03)
    print(problem04)

    name = "황승재"
    affiliation = "스마트팜학과"
    student_id = "202217737"

    answer1 = problem01
    answer2 = problem02
    answer3 = problem03
    answer4 = problem04
    print(f"제출코드 : {problem01}, {problem02}, {problem03}, {problem04}.")
    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)

if __name__ == "__main__":
    main()