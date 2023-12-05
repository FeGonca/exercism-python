"""Functions to help armstrong-numbers.
"""

def is_armstrong_number(number):
    """
    Check if the number is Armstrong

    :param number: int - given number.
    :return: bool
    """
    
    strNum = str(number)
    lenNum = len(strNum)

    sum = 0
    for i in range(lenNum):
        temp = int(strNum[i]) ** lenNum
        sum += temp
    
    if (sum == number):
        return True
    return False
