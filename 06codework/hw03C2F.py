def c2f(x):
     return x*1.8 + 32

temp_c = float(input("몇도인데요?"))
temp_f = c2f(temp_c)

print(f"{temp_c}℃ => {temp_f}℉")