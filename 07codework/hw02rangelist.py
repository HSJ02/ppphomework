def get_range_list(n):
    result = []
    for i in range(0, n+1):
        result.append(i)
    return result
    

def main():
    x = int(input("정수를 주세요. 리스트 만들어서 드릴게요!!"))
    print(f"결과는 아래에 ㅎㅎ \n => {get_range_list(x)}")

if __name__ == "__main__":
    main()