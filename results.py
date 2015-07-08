import calculations


def checkWeight(weight, height):
    '''
    :param height: зріст
    :param weight: вага
    :return: 0, якщо вага ідеальна; 1, якщо більша ідеальної;
             -1, якщо менша ідеальної
    '''
    if calculations.getIdealWeightLorentz(height) > weight:
        return -1
    elif calculations.getIdealWeightLorentz(height) == weight:
        return 0
    return 1


def checkBMI(weight, height):
    '''
    :param weight: вага
    :param height: зріст
    :return: стан здоров'я від -2 до 5, де 5 -- ожиріння
    '''
    result = calculations.getBMI(height, weight)
    if result < 17.5:
        return -2
    elif result < 19.5:
        return -1
    elif result < 22.9:
        return 0
    elif result < 27.4:
        return 1
    elif result < 30:
        return 2
    elif result < 35:
        return 3
    elif result < 40:
        return 4
    return 5

