import random

def check(solution, answer, input_ch):

    is_correct = False
    for i in range(len(solution)):
        if solution[i] == input_ch:
            if answer[i] == "_":
                answer[i] = solution[i]
                is_correct = True
                break

    return is_correct



def main():
    problems = ["apple", "banana"]

    solution = problems[random.randrange(len(problems))]
    is_correct = False
    Lives = 5 # 목숨은 5개~
    
    answer = []
    for n in range(len(solution)):
        answer.append("_")
    # print(answer)

    while True: 
        input_ch = input(f"{''.join(answer)}? => ")

        if check(solution, answer, input_ch):
            print(f"{input_ch}(이)가 포함됐네요!")
            print(f"남은 목숨은 {Lives}!!")
        else:
            Lives -= 1
            print(f"이런.. 틀렸네요 ㅠㅠ. 남은 목숨은 {Lives}!!")
        
        if "_" not in answer:
            is_correct = True
            break

        if Lives <= 0:
            break

    if is_correct:
        print(f"\n정답은 {solution}입니다.")
        print("잘하셨습니다.")
    else:
        print("아쉽군요.")

if __name__ == "__main__":
    main()

