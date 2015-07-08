def get_weight_recommendations(result):
    """
    :param result: результат порівняння заданої ваги з ідеальною вагою
    :return: вага у порівнянні з ідеалом
    """
    recommendations = {
        "-1": "Your weight below the ideal",
        "0": "Your weight is ideal",
        "1": "Your weight above the ideal"
    }
    return recommendations[result]

def get_bmi_recommendations(bmi):
    '''
    :param bmi: значення BMI
    :return: стан здоров'я і рекомендації
    '''
    recommendations = {
        "-2": "Anorexia. Recommended weight gain.",
        "-1": "Deficiency of body weight.",
        "0": "Normal",
        "1": "Excess body weight. Recommended weight loss.",
        "2": "Obesity I degree. Recommended weight loss.",
        "3": "Obesity II degree. It is highly recommended weight loss.",
        "4": "Obesity III degree. It is highly recommended weight loss.",
        "5": "Obesity IV degree. Need immediate weight loss."
    }
    return recommendations[bmi]

