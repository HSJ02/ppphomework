n = int(input("몇까지 더하고 싶어용?"))
numbers = range(1,n+1)


def sum_n(n): 
    total = 0
    for s in n:
        total += s
    return total 

print(sum_n(numbers))
