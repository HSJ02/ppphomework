# 자료를 끌어와서, 칼로리 계산 프로그램 만들기.
def read_db(filename):
    kcal_dic = {}
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",") # ,를 기준으로 자르겠다. 나누겠다.
            kcal_dic[tokens[0]] = int(tokens[1])

    return kcal_dic

def main():
    # 딕셔너리 to 계산 
    #fruit_kcal = {"보리" : 300, "바나나" : 100}
    fruit_kcal = read_db("codework09/calorie_db.csv")
    fruit_gram = {"보리" : 160, "바나나" : 200 }

    total = 0
    for chunk in fruit_gram:
        total += fruit_gram[chunk]*fruit_kcal[chunk]/100
        
    print(f"총 섭취 칼로리는 {total} kcal입니다.")


if __name__ == "__main__":
    main()

