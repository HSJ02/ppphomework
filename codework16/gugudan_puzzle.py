import random

def problem():
    dan = random.randint(2, 9)
    mul = random.randint(1, 9)

    try:
        answer = int(input(f"{dan} x {mul} => "))
    except ValueError:
        return False
    
    if answer == dan * mul:
        return True
    return False


def main():
    score = 0
    total_problem = 5
    for n in range(5):
        is_correct = problem()
        if is_correct:
            score += 1
    print(f"맞춘 개수는 {score}개, 총점은 {score/ total_problem*100}점")

if __name__ == "__main__":
    main()