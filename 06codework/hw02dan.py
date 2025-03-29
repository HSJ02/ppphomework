gugu = int(input("몇단을 구하시겠어요?"))

def dan(gugudan):
    answer = n*gugudan
    return answer

for i in range(9):
    n = i+1
    print(f"{gugu}x{n}={dan(gugu)}")