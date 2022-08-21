def sum_numbers(*num: float) -> float:
    """
    calculating sum of passed number.

    :param num:
    :return:
    """
    total = 0
    for i in num:
        total += i
    return total

