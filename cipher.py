#Core Algorithm
def caesar_cipher(text: str, shift: int, mode: str = 'encrypt') -> str:
    """Core Encryption/Decryption Function"""
    if not isinstance(shift, int):
        raise ValueError("Shift must be an integer")

    if shift < 1 or shift > 26:
        raise ValueError("Shift must be between 1 and 26")

    result= []

    for char in text:
        if char.isalpha():
                #Determine base ASCII value
            base = ord('A') if char.isupper() else ord('a')
                #Calculate the shifted character
            shifted = ord(char) - base 
            offset = shift if mode == 'encrypt' else -shift
            new_char = chr((shifted + offset) % 26 + base)
            result.append(new_char)
        else:
                 #keeps the non-alphabetic characters
            result.append(char)
            
    return ''.join(result)