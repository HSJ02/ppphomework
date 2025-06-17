import matplotlib.pyplot as plt
import csv
import koreanize_matplotlib

# 감정별 누적합
total_happiness = 0
total_uneasiness = 0
total_sadness = 0
total_wariness = 0
total_anger = 0

# CSV 경로
csv_file = "project/emotions_2024_simulated.csv"

with open(csv_file, encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        total_happiness += int(row[3])
        total_uneasiness += int(row[4])
        total_sadness += int(row[5])
        total_wariness += int(row[6])
        total_anger += int(row[7])

# 라벨과 값
labels = ['행복', '불안', '슬픔', '경계심', '분노']
values = [total_happiness, total_uneasiness, total_sadness, total_wariness, total_anger]
colors = ['#FF6B6B', '#A0A0A0', '#4A90E2', '#9B59B6', '#F5B041']

# 파이 그래프 (원형, 퍼센트 안쪽, 글씨 큼)
plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(
    values,
    labels=labels,
    colors=colors,
    autopct='%.1f%%',
    startangle=90,
    textprops={'fontsize': 20},
    pctdistance=0.7  # 퍼센트 안쪽에 배치
)

# 라벨 텍스트 키우기
for text in texts:
    text.set_fontsize(20)

# 그래프 타이틀
plt.title("2024년 감정 비율 (5개 감정 원형)", fontsize=18)
plt.tight_layout()
plt.savefig("emotion_pie_5types.png")
plt.show()