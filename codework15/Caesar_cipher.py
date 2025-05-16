def caesar_decode(text : str, shift : int = 3):
     return caesar_encode(text, -shift)

def spacebar(bar):
    full_text = []
    for ch in bar:
        if ch == "#":
            spacebar = caesar_decode(ch)
            full_text.append(spacebar)
        else:
            full_text.append(ch)
    return "".join(full_text)

def caesar_encode(text : str, shift : int = 3):
    full_text = []
    xyz_list = ['x', 'y', 'z']
    XYZ_list = ['X', 'Y', 'Z']
    for ch in text:
        if not ch in XYZ_list:
            if not ch in xyz_list:
                encoded_ch = chr(ord(ch)+shift)
                full_text.append(encoded_ch)
            elif ch in xyz_list:
                encoded_ch = chr(ord(ch)-23)
                full_text.append(encoded_ch)
        elif ch in XYZ_list:
            encoded_ch = chr(ord(ch)-23)
            full_text.append(encoded_ch)

    return "".join(full_text) # 빈칸으로 텍스트 다 붙이기

def main():
    text = input("문장을 입력하세요:")
    print(spacebar(caesar_encode(text)))

if __name__ == "__main__":
    main()