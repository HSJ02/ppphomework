import random
from rich import print
import PySimpleGUI as sg


def get_lotto():
    lotto_list = []
    while True:
        n = random.randint(1,45)
        if n not in lotto_list:
            lotto_list.append(n)

        if len(lotto_list) == 6:
            break

    return lotto_list

def main():
    lotto_num_list = []
    correct_nums_list = []
    choice_nums = sg.popup_get_text("숫자 6개를 넣어보세용 (예: 1, 2, 3...) : ", title="로또")
    choice_nums = choice_nums.strip()
    choice_nums_list = choice_nums.split(",")

    for i in range(5):
        lotto_num = get_lotto()
        lotto_num_list.append(lotto_num)
        print(lotto_num)
    for num in lotto_num_list:
        for cho_nums in choice_nums_list:
            if int(cho_nums) in num:
                correct_nums_list.append(int(cho_nums))
                break
    if not correct_nums_list:
        print("아쉽군요. [bold red]당첨 0개..")
    elif correct_nums_list:
        print(f"축하드려요. [bold red]{len(correct_nums_list)}개 당첨~[/bold red]")
    
if __name__ == "__main__":
    main()