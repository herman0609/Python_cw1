def ext_vigenere(text, key, option):
    key_clone = key
    if len(key_clone) >= len(text):
        key_clone = key_clone[:len(text)]
    else:
        while len(key_clone) < len(text):
            key_clone = key_clone+key
        key_clone = key_clone[:len(text)]

    if option.lower() == "encrypt":
        result = ""
        for i in range(0, len(text)):
            new_text = chr(((ord(text[i])-32) +
                            (ord(key_clone[i])-32)) % 95 + 32)
            result = result + new_text
    elif option.lower() == "decrypt":
        result = ""
        for i in range(0, len(text)):
            new_text = chr(((ord(text[i]) - 32) -
                            (ord(key_clone[i]) - 32)) % 95 + 32)
            result = result + new_text
    else:
        result = "Invalid option!"
    return result
