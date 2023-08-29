def decrypt(encrypted_text):
    key = "@dicky-alfansyah"
    decrypted_text = ""
    key_index = 0

    for char in encrypted_text: 
        unicode_val = ord(char)
        key_val = ord(key[key_index % len(key)])
        xor_val = unicode_val - 12353
        xor_val = xor_val ^ key_val
        decrypted_char = chr(xor_val)
        decrypted_text += decrypted_char
        key_index += 1
    return decrypted_text

def main():
    encrypted_text = "おゅてきぞそぎべいごもちぇがさぅァてごかげすゆも坉"
    decrypted_text = decrypt(encrypted_text)

    print("Teks :", decrypted_text)
    
if __name__ == "__main__":
    main()
