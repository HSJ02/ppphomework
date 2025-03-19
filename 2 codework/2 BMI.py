weight = int(input("몸무게(kg)는 얼마에요? => "))
height = int(input("키(cm)가 얼마인가요? => "))

height_m = height / 100

BMI = weight / height_m ** 2  

print("키는 {}cm, 몸무게는 {}kg일 때, BMI는 {}입니다.".format(height, weight, BMI))