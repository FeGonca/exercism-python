def is_valid(isbn):
    isbn = isbn.replace("-", "")

    if not isbn or len(isbn) != 10:
        return False

    i = 0
    multi = 10
    sum = 0

    while i < 10:

        if isbn[i].isdigit():
            sum += int(isbn[i]) * multi            
            i += 1
            multi -= 1
            

        elif isbn[-1] == 'X':
                sum += 10 * multi                
                i += 1
                multi -= 1
                
        else:
             return False
        
    return sum % 11 == 0