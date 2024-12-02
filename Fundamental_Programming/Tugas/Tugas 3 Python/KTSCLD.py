def vigenere_cipher(message, key, mode):
    result = []
    key_index = 0
    for char in message:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if mode == 0:  # Enkripsi
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:  # Dekripsi
                new_char = chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            result.append(new_char)
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)

key = 'TRUESKILL'
print(f"Kata kunci Vigenère cipher: {key}")

T = int(input())
for i in range(T):
    mode = int(input())
    message = input().strip()
    if mode == 0 or mode == 1:
        result = vigenere_cipher(message, key, mode)
        print(result)
    else:
        print("Gunakan 0 untuk enkripsi atau 1 untuk dekripsi.")
