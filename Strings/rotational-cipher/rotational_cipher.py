def rotate(text, key):
    result = ''

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            index = ord(char.lower()) - ord('a')
            rotated_index = (index + key) % 26
            rotated_char = chr(rotated_index + ord('a'))
            result += rotated_char.upper() if is_upper else rotated_char
        else:
            result += char
    return result
