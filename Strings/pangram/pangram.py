def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    i = 0

    while i < len(alphabet):
        if alphabet[i] not in sentence:
            return False
        i += 1

    return True