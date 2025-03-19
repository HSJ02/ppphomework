print("\n안녕하세요 두점 사이의 거리를 구해볼까요?\n각 P의 위치에 좌표를 기억해두세요.\n")

fPx = float(input("첫 번째 P의 x축 좌표를 기입하세요."))
fPy = float(input("첫 번째 P의 y축 좌표를 기입하세요."))

print("\n잘하셨어요. 입력되었습니다. 두 번째 P의 좌표를 적어봅시다!\n")

sPx = float(input("두 번째 P의 x축 좌표를 기입하세요."))
sPy = float(input("두 번째 P의 y축 좌표를 기입하세요."))

square_of_DISTANCE = (sPx-fPx)**2 + (sPy-fPy)**2
Real_Distance = square_of_DISTANCE**(1/2)

print("\n좋아요 정리해줄게요\n\n첫 번째 P의 좌표는({},{})\n두 번째 P의 좌표는({},{})입니다.".format(fPx, fPy, sPx, sPy))
print("\n두 점 사이의 거리는 '{}'입니다.".format(Real_Distance))

