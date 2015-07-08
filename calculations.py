def get_ideal_weight_lorentz(height):
    """
    :param height: зріст
    :return: ідеальна вага для заданого зросту
    """
    height = is_heightIn_centimetres(height)
    weight = (height - 100) - (height - 150)/2.0
    return weight


def get_bmi(height, weight):
    '''
    :param height: зріст
    :param weight: вага
    :return: індекс маси тіла
    '''
    height_in_meters = is_heightIn_centimetres(height) / 100.0
    bmi = weight / height_in_meters ** 2
    return bmi


def get_ideal_weight_nagler(height):
    '''
    :param height: зріст
    :return: ідеальна вага за Наглером
    '''
    mass = 45
    height = is_heightIn_centimetres(height)
    difference = height - 152.4
    mass += difference/2.45 * 0.9
    mass += mass * 0.1
    return mass


def is_heightIn_centimetres(height):
    '''
    :param height: зріст
    :return: зріст в сантиметрах
    '''
    if height < 10:
        return height * 100
    return height

