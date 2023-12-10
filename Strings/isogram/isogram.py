def is_isogram(string):
    string = ''.join(e for e in string if e.isalnum()).lower()    
    
    return len(string) == len(set(string))