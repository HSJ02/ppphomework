import math

r = int(input("반지름은 얼마인가요? => "))
pi = math.pi
round = 2*pi*r
area = pi * (r**2)

print(f"반지름이 {r}인 원의 둘레는 {round:.1f}입니다.")
print(f"반지름이 {r}인 원의 면적은 {area:.3f}입니다.")
