def caesarCipher(text, shift, mode):
    result = []
    for char in text:
        if char.isalpha():
            ascii_A = 65 if char.isupper() else 97
            if mode == 1:  # Enkripsi
                newChar = chr((ord(char) - ascii_A + shift) % 26 + ascii_A)
            else:  # Dekripsi
                newChar = chr((ord(char) - ascii_A - shift) % 26 + ascii_A)
            result.append(newChar)
        else:
            result.append(char)
    return ''.join(result)

# Inputan
mode, shift = map(int, input().split())
shift %= 26  # Supaya pergeseran terus bisa diulang di antara karakter huruf

texts = []
while True:
    text = input()
    if text.strip().upper() == 'EOF': # Untuk menghilangkan spasi di awal dan akhir serta membuat semua huruf menjadi uppercase
        break # Break untuk menghentikan proses input ketika bertemu kata EOF
    texts.append(text)
    
for text in texts:
    print(caesarCipher(text, shift, mode))
