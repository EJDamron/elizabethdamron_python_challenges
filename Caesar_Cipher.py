def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += new_char
        else:
            result
    
    return result

# Demo code
if __name__ == "__main__":
    examples = [
        ("abc", 3),
        ("xyz", 2),
        ("Hello, World!", 5),
        ("Python 3.10", 4)
    ]

    for text, shift in examples:
        encoded = caesar_cipher(text, shift)
        print(f"Original: {text}")
        print(f"Shift {shift}: {encoded}")
        print()