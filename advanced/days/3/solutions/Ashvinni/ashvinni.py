def decrypt_message(message):
    vowels = ['A', 'E', 'I', 'O', 'U']
    decrypted_message = ''
    number = ''
    has_number = False
    has_symbol = False
    
    for char in message:
        if char.isalpha():
            if char.upper() in vowels:
                decrypted_message += vowels[(vowels.index(char.upper()) + 1) % 5] if char.islower() else vowels[(vowels.index(char.upper()) + 1) % 5].lower()
            else:
                decrypted_message += chr(ord(char) - ord('1') + ord('A'))
        elif char.isdigit():
            number += char
            has_number = True
        elif char == '|':
            if number:
                if number.endswith('_'):
                    decrypted_message += chr(int(number[:-1]) + 1 + ord('A'))
                else:
                    decrypted_message += chr(int(number) - 1 + ord('A'))
                number = ''
                has_number = False
        else:
            symbol_number = ord(char) - ord('!')
            decrypted_message += chr(symbol_number - 1 + ord('A')) if symbol_number > 0 and symbol_number < 11 else char
            has_symbol = True
    
    if not has_number and not has_symbol:
        return decrypted_message.strip()
    else:
        return decrypted_message


encrypted_message = "*U22|% ! 18|_U^% !14|$ 13|%17|_18|25| #*17|_E19|19|_13|!19|."
decrypted_message = decrypt_message(encrypted_message)
print(decrypted_message)
