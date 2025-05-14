# 자연수만 받아보기 
def average(nums):
    return sum(nums)/len(nums)

def str2N(nums_list: list):
    real_list = []
    for num in nums_list:
        try:
            n = int(num)
            if n > 0:
                real_list.append(n)
                
        except ValueError:
            print(f"자연수 아님 >>> {num}을 무시하겠음!!")
    return real_list

def makelist(nums):
    nums_list = []
    for num in nums:
        nums_list.append(num.strip())
    return nums_list

def main():
    nums = input("숫자를 나열해주세요 (예: 10, 20, 30)")
    nums = nums.split(",")
    nums_list = makelist(nums)
    N_list=str2N(nums_list)

    print(f"입력된 값은 {N_list}입니다. 총 {len(N_list)}개의 자연수가 입력되었고, 평균은 {average(N_list)}입니다.")
   
if __name__ == "__main__":
    main()
