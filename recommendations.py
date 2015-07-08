def getWeightRecommendations(result):
    """
    :param result: результат порівняння заданої ваги з ідеальною вагою
    :return: вага у порівнянні з ідеалом
    """
    recomm = {
        "-1": "Your weight below the ideal",
        "0": "Your weight is ideal",
        "1": "Your weight above the ideal"
    }
    return recomm[result]

def getBMIRecommendations(bmi):
    '''
    :param bmi: значення BMI
    :return: стан здоров'я і рекомендації
    '''
    recomm = {
        "-2": "Anorexia. Recommended weight gain.",
        "-1": "Deficiency of body weight.",
        "0": "Normal",
        "1": "Excess body weight. Recommended weight loss.",
        "2": "Obesity I degree. Recommended weight loss.",
        "3": "Obesity II degree. It is highly recommended weight loss.",
        "4": "Obesity III degree. It is highly recommended weight loss.",
        "5": "Obesity IV degree. Need immediate weight loss."
    }
    return recomm[bmi]
