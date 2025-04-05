def total_calorie(fruits, fruits_calorie_dic):
    total = 0
    for fruit in fruits:

        if fruit == "딸기":
            total += fruits["딸기"]*fruits_calorie_dic["딸기"]/100
        elif fruit == "한라봉":
            total += fruits["한라봉"]*fruits_calorie_dic["한라봉"]/100
        elif fruit == "바나나":
            total += fruits["바나나"]*fruits_calorie_dic["바나나"]/100
        else:
            return("칼로리 정보가 없습니다.")
        
    return total

def main():
    fruits = {"딸기": 300, "한라봉": 150}
    fruits_calorie_dic = {"한라봉": 50, "딸기": 34, "바나나": 77}

    print(f"총 섭취 칼로리는 {total_calorie(fruits, fruits_calorie_dic)} kcal입니다.")

if __name__ == "__main__":
    main()