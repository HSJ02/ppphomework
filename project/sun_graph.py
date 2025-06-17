import matplotlib.pyplot as plt
import csv
import koreanize_matplotlib

monthly_happiness = [0] * 12
monthly_uneasiness = [0] * 12
monthly_negative = [0] * 12  

csv_file = "project/emotions_2024_simulated.csv"

with open(csv_file, encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        month = int(row[1]) - 1
        monthly_happiness[month] += int(row[3])
        monthly_uneasiness[month] += int(row[4])
        monthly_negative[month] += int(row[5]) + int(row[6]) + int(row[7])

months = [f"{i+1}월" for i in range(12)]

plt.figure(figsize=(14, 7))

plt.plot(months, monthly_happiness, label="행복", color="red", marker='o', linewidth=2)
plt.plot(months, monthly_uneasiness, label="불안", color="black", marker='o', linewidth=2)
plt.plot(months, monthly_negative, label="부정적인 감정", color="blue", marker='o', linewidth=2)

plt.title("2024년 월별 감정 도합 추이 (선 그래프 버전)")
plt.xlabel("월")
plt.ylabel("감정 도합 점수")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("emotion_monthly_line_only.png")
plt.show()