from hw01average import average

def main():
    text = input("정수 값을 나열해주세요 (예시: 10 20 30) : ")
    text_list = text.split()

    n = []
    for x in text_list:
        n.append(int(x))

    print(average(n))

if __name__ == "__main__":
    main()