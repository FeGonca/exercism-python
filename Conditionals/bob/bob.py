def response(hey_bob):
    if not hey_bob.strip():
        return "Fine. Be that way!"
    
    hey_bob = hey_bob.strip()
    
    if hey_bob.endswith('?'):
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    
    if hey_bob.isupper():
        return "Whoa, chill out!"
    
    return "Whatever."
