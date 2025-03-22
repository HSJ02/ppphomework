print("\n안녕하세요 몇 사분면에 있는 지를 구해볼까요?\n각 P의 위치에 좌표를 기억해두세요.\n")

Px = float(input("첫 번째 P의 x축 좌표를 기입하세요."))
Py = float(input("첫 번째 P의 y축 좌표를 기입하세요."))

print("\n잘하셨어요. 입력되었습니다.\n")

if Px/abs(Px) + Py/abs(Py) == 2:
    print("제 1사분면 입니다.")
elif Px/abs(Px) + Py/abs(Py) == -2:
    print("제 3사분면 입니다.")
elif Px/abs(Px) - Py/abs(Py) == -2:
    print("제 2사분면 입니다.")
elif Px/abs(Px) - Py/abs(Py) == 2:
    print("제 4사분면 입니다.")
