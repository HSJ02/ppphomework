print("안녕하세요. 다이어트 도우미에요.")
print("오늘 섭취한 칼로리 알아봅시다~!\n")

Kcal_per100= {'H' : 50, 'S' : 34, 'B' : 77 }

Hallabong_m = float(input("오늘 드신 한라봉의 무게(g)가 몇인가요?"))
Strawberry_m = float(input("오늘 드신 딸기(설향)의 무게(g)가 몇인가요?"))
Banana_m = float(input("오늘 드신 바나나의 무게(g)가 몇인가요?"))

H_Kcal = Hallabong_m * Kcal_per100["H"] / 100
S_Kcal = Strawberry_m * Kcal_per100["S"] / 100
B_kcal = Banana_m* Kcal_per100["B"] / 100 
Total_kcal = H_Kcal + S_Kcal + B_kcal

print("\n섭취한 한라봉의 양 => {}g\n섭취한 딸기(설향)의 양 => {}g\n"
"섭취한 바나나의 양 => {}g\n"
.format(Hallabong_m, Strawberry_m, Banana_m))

print("당신께서 오늘 섭취하신 \n'한라봉' 칼로리는 => {} Kcal,\n'딸기(설향)' 칼로리는 => {} Kcal,\n"
"'바나나' 칼로리는 => {} Kcal\n\n"
"당신이 위 과일로 섭취한 '총 칼로리'는 => {} Kcal\n맛있었겠네요 :) 나도 좀 나눠줘요~"
.format(H_Kcal, S_Kcal, B_kcal, Total_kcal))