from hw01average import average

def main():
    text = input("정수를 순서대로 기입하세요. 예시(10 20 30) : ")
    text_list = text.split()

    nums = []
    for x in text_list:
        nums.append(int(x))

    print(f"평균은 {average(nums):.1f}입니다.")

if __name__ == "__main__":
    main()