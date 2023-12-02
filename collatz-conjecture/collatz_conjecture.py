def steps(number):
    try:
        number / 1
    except ValueError as e:
        return f"Only positive integers are allowed"

    if number <= 0:
        raise ValueError('Only positive integers are allowed')

    result = False
    qtd = 0

    while not result:
        if number == 1:
            result = True
            break
            
        if number % 2 == 0:            
            number = number / 2
            qtd += 1
            if number == 1:
                result = True
        else:
            number = ((3 * number) + 1)
            qtd += 1
                
    return qtd
