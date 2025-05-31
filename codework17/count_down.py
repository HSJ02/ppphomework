import time
import PySimpleGUI as sg
from rich import print



def count_down(count):
    for i in range(count):
        print(f"[bold red]{count - i}...", end="\r")
        time.sleep(0.7)
    print("[bold red]Bomb!!")


def main():
    num = int(sg.popup_get_text("숫자를 입력하시오", title="카운트다운"))
    print(count_down(num))

if __name__ == "__main__":
    main()