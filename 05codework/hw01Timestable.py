dan = int(input("구구단을 외자! 구구단을 외자!\n몇단이 궁금하세요?"))

for i in range(9):
    print(f"{dan}x{i + 1} = {dan*(i+1)}")