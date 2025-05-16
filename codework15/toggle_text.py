def toggle_text(text: str) -> str:
    text_list = []
    for ch in text:
        if 'a' <= ch <= 'z':
            upper_ch = chr(ord(ch) - 32)
            text_list.append(upper_ch)
        elif 'A' <= ch <= 'Z':
            lower_ch = chr(ord(ch) + 32)
            text_list.append(lower_ch)
        else:
            text_list.append(ch)
    return "".join(text_list)


def main():
    text = input("알파벳을 임의로 나열해주세요 : ")
    print(toggle_text(text))



if __name__ == "__main__":
    main()