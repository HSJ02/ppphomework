import random

def to_chosung_ch(ch):
    
    chosung_list = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ',
    'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ',
    'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]
    Hangeul_num = (ord(ch) - ord('가'))//588

    return chosung_list[Hangeul_num]

def to_chosung(text):
    full_text = []
    for ch in text:
        full_text.append(to_chosung_ch(ch))
    return full_text


def main():
    problems = ["바나나", "딸기", "토마토", "복숭아"]
    

    solution = problems[random.randrange(len(problems))]
    while True:
        Q = "".join(to_chosung(solution))
        answer = input(f"{Q}? => ")
        if answer == solution:
            print("정답입니다.")
            break
        else:
            print("오답입니다.")

if __name__ == "__main__":
    main()

