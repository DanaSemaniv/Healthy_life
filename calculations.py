def getIdealWeightLorentz(height):
    """
    :param height: зріст
    :return: ідеальна вага для заданого зросту
    """
    height = isHeightInСentimetres(height)
    weight = (height - 100) - (height - 150)/2.0
    return weight


def getBMI(height, weight):
    '''
    :param height: зріст
    :param weight: вага
    :return: індекс маси тіла
    '''
    height_in_meters = isHeightInСentimetres(height) / 100.0
    bmi = weight / height_in_meters ** 2
    return bmi


def isHeightInСentimetres(height):
    '''
    :param height: зріст
    :return: зріст в сантиметрах
    '''
    if height < 10:
        return height * 100
    return height
