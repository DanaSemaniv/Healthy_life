import calculations


def checkWeight(weight, height):
    '''
    :param height: ?????
    :param weight: ????
    :return: 0, ???? ???? ????????; 1, ???? ?????? ?????????;
             -1, ???? ????? ?????????
    '''
    if calculations.getIdealWeightLorentz(height) < weight:
        return -1
    elif calculations.getIdealWeightLorentz(height) == weight:
        return 0
    return 1


def checkBMI(weight, height):
    '''
    :param weight: ????
    :param height: ?????
    :return: ???? ??????'? ??? -2 ?? 5
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

