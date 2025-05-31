import random
from rich import print
import PySimpleGUI as sg


def problem():
    dan = random.randint(2, 9)
    mul = random.randint(1, 9)

    try:
        answer = int(sg.popup_get_text(f"{dan} x {mul} ?", title="구구단"))
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
    print(f"맞춘 개수는 [bold red]{score}개[/bold red], 총점은 [bold red]{score/ total_problem*100}점[/bold red]")

if __name__ == "__main__":
    main()