import calculations
import recommendations
import levitsky_table


def check_weight_lorentz(weight, height):
    '''
    :param height: зріст
    :param weight: вага
    :return: 0, якщо вага ідеальна; 1, якщо більша ідеальної;
             -1, якщо менша ідеальної
    '''
    out = ""
    if calculations.get_ideal_weight_lorentz(height) > weight:
        out = "-1"
    elif calculations.get_ideal_weight_lorentz(height) == weight:
        out = "0"
    else:
        out = "1"
    return "Lorentz formula: " + recommendations.get_weight_recommendations(out)


def check_bmi(weight, height):
    '''
    :param weight: вага
    :param height: зріст
    :return: стан здоров'я від -2 до 5, де 5 -- ожиріння
    '''
    result = calculations.get_bmi(height, weight)
    out = ""
    if result < 17.5:
        out = "-2"
    elif result < 19.5:
        out = "-1"
    elif result < 22.9:
        out = "0"
    elif result < 27.4:
        out = "1"
    elif result < 30:
        out = "2"
    elif result < 35:
        out = "3"
    elif result < 40:
        out = "4"
    else:
        out = "5"
    return "Body mass index: " + recommendations.get_bmi_recommendations(out)


def check_weight_nagler(weight, height):
    '''
    :param weight: зріст
    :param height: вага
    :return: 0, якщо вага ідеальна; 1, якщо більша ідеальної;
             -1, якщо менша ідеальної
    '''
    out = ""
    if calculations.get_ideal_weight_nagler(height) > weight:
        out = "-1"
    elif calculations.get_ideal_weight_nagler(height) == weight:
        out = "0"
    else:
        out = "1"
    return "Nagler formula: " + recommendations.get_weight_recommendations(out)

def check_weight_levitsky(height, weight, age, sex):
    '''
    :param height: зріст
    :param weight: вага
    :param age: вік
    :param sex: стать
    :return: 0, якщо вага максимальна; 1, якщо більша максимальної;
             -1, якщо менша максимальної
    '''
    out = ""
    height = calculations.is_heightIn_centimetres(height)
    if levitsky_table.get_maximum_weight(sex, height, age) > weight:
        out = "-1"
    elif levitsky_table.get_maximum_weight(sex, height, age) == weight:
        out = "0"
    else:
        out = "1"
    return "According to the Levitsky table your weight is " + \
           recommendations.compare_with_max(out)