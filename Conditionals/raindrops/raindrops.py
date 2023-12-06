def convert(number):
    response = ''.join(sound for divisor, sound in [(3, 'Pling'), (5, 'Plang'), (7, 'Plong')] if number % divisor == 0)
    return response or str(number)
