def substract(L1, L2):
    """
    Bouarioua Mohamed cherif
    """
    result = []
    for element in L1:
        if element not in L2:
            result.append(element)
    return result
