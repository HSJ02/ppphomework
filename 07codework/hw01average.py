# 어떤 집합리스트가 있을 때 평균을 구해보자 !!

def average(nums):
    total = 0
    for num in nums:
        total = num + total 

    total_x = 0
    for i in nums:
         total_x += 1
         
    av = total / total_x
    return av

def main():
    x = [1, 2, 3, 4, 5, 6, 7, 10]
    print(f"평균은 {average(x)}입니다.")


if __name__ == "__main__":
    main()