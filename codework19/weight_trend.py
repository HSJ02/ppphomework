import matplotlib.pyplot as plt
import numpy as np
import koreanize_matplotlib

def main():
    labels = [
        "4/6", "4/14", "4/22", "5/7", "5/16", "5/22", "6/4",
        "6/14", "6/19", "7/4", "7/11", "7/13", "7/22", "7/27",
        "8/1", "8/8", "8/12", "8/17", "8/24", "8/31", "9/7",
        "9/14", "9/21", "9/28", "10/5", "10/12", "10/18", "10/26",
        "11/2", "11/9", "11/16", "11/23"
    ]

    weights = [
        75.0, 74.5, 74.3, 73.4, 73.0, 72.7, 72.8, 72.0, 71.5, 70.2,
        69.2, 68.6, 67.7, 67.5, 67.0, 66.4, 66.1, 65.7, 65.1, 64.05,
        63.8, 62.8, 62.3, 61.9, 61.0, 60.4, 59.9, 59.2, 58.9, 58.0,
        58.0, 57.0
    ]

    x = np.arange(len(labels))
    y = np.array(weights)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(x, y, color='red', marker='o', label='체중 변화')

    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45)

    # 제목 및 축 라벨
    ax.set_title("몸무게 추이 그래프")
    ax.set_xlabel("날짜")
    ax.set_ylabel("체중(kg)")

    # 격자 및 범례
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.savefig("./line_weight.png")

if __name__ == "__main__":
    main()