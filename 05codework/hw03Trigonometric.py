# 삼각함수 표 만들기 ~ !
import math

# radian = math.radians # 각도

for i in range(361):
    radian = math.radians(i)
    sin = math.sin(radian)
    cos = math.cos(radian)
    
    if abs(cos) < 0.00001:
        tan = "무한대"
        realtan = tan
    else:
        tan = sin/cos
        realtan = f"{tan:.2f}"
    
    print(f"|  sin  |  cos  |  tan |→{i}°\n| {sin:.2f} | {cos:.2f} | {realtan} |")



