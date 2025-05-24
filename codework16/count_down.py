import time

def count_down(count):
    for i in range(count):
        print(f"{count - i}...", end="\n\r")
        time.sleep(1)
    print("Bomb!!")


def main():
    num = int(input("숫자를 입력하시오"))
    print(count_down(num))

if __name__ == "__main__":
    main()