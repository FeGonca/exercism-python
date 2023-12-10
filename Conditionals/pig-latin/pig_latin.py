def translate(text):    
    translated_words = []
    
    for word in text.split():
        translated_word = pig_latin(word)
        translated_words.append(translated_word)

    return ' '.join(translated_words)

def pig_latin(word):
    vowels = 'aeiou'
    # Rule 1
    if word[0] in vowels or word[:2] in ['xr', 'yt']:
        return word + 'ay'
    
    #Rule 3
    if 'qu' in word:
        index = word.index('qu') + 2
        return word[index:] + word[:index] + 'ay'
    
    # Rule for 'thr' at the beginning
    if word[:3] == 'thr':
        return word[3:] + 'thray'
    
    # Rule for 'th' at the beginning
    if word[:2] == 'th':
        return word[2:] + 'thay'
    
    #Rule 4
    if 'y' in word[1:]:
        index = word.index('y')
        return word[index:] + word[:index] + 'ay'
    
    #Rule 2
    consonant_sound = ''
    index = 0
    while index < len(word) and word[index] not in vowels:
        consonant_sound += word[index]
        index += 1
    
    return word[index:] + consonant_sound + 'ay'