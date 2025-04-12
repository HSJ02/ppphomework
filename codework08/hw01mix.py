def read_text(filename):
    text=""
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            
            text += " " + line.strip()
    return text


def read_numbers(filename):
    nums = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            nums.append(int(line.strip()))
    return nums

def total_list(num):
    total = 0
    for b in num:
        total += 1
    return total

def text2list(nums):
    nums_list = nums.split()

    num = []
    for i in nums_list:
        num.append(int(i))
    return num

def average(nums):
    total = 0
    for num in nums:
        total = num + total 

    total_x = 0
    for i in nums:
         total_x += 1
         
    av = total / total_x
    return av

def median(x):
    x_list = x.split()
    num = []
    for i in x_list:
        num.append(int(i))
    
    num_orm = sorted(num)

    total = 0
    for b in num:
        total += 1
        
    if total%2 == 1: # 홀수
        result = total//2 
        return num_orm[result]
    elif total%2 == 0: # 짝수
        result1 = int(total/2)-1
        result2 = int(total/2 +1)-1
        realresult = (num_orm[result1] + num_orm[result2])/2
        return realresult

def minmax(nums):
    
    return max(nums), min(nums)


def main():
    #text = "5 10 3 4 7"
    filename = "codework08/test.txt"
    num = read_text(filename)
    #nums2 = "1 2 3 4 5 6 7 8 9 10 11"
    nums1 = num
    mx, mn = minmax(text2list(nums1))
    print(f"총 숫자의 갯수는{total_list(text2list(nums1))}개이다.")

    print("최댓값은", mx)
    print("최솟값은", mn)

    print("평균값은 {:.1f}".format(average(text2list(nums1))))
    print("중앙값은 {}".format(median(nums1)))
    print(num)


    

if __name__ == "__main__":
    main()