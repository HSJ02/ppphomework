def is_leap_year(y):
    if y%4 > 0:
        return "False"
    elif y%100 == 0:
        return ("False")
    else:
        return ("True")


def main():
    x = int(input("궁금하신 년도를 기입하세요."))
    print(f"{x}년은 윤년일까요? 결과 => {is_leap_year(x)}!")

if __name__ == "__main__":
    main()