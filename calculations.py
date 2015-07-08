def getIdealWeightLorentz(height):
    """
    :param height: зріст
    :return: ідеальна вага для заданого зросту
    """
    weight = (height - 100) - (height - 150)/2.0
    return weight

def getBMI(height, weight):
    '''

    :param height: зріст
    :param weight: вага
    :return: індекс маси тіла
    '''
    height_in_meters = height / 100
    bmi = weight / height_in_meters ** 2
    return bmi
