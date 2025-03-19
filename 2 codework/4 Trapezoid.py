upper = int(input("윗변의 길이를 알려주세요 => "))
lower = int(input("밑변의 길이를 알려주세요 => "))
height = int(input("마지막으로 높이를 알려주세요 => "))
area = (upper + lower)*height/2

print("윗변={}, 밑변={}, 높이={}일 때,".format(upper, lower, height))
print("사다리꼴의 넓이 => {}".format(area))
