star = "*"
spacebar = " "
for i in range(10):
    n = i + 1
    m = n - 10
    print(f"{spacebar*abs(m)}{star*n}")