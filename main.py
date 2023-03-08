def substract(L1, L2):
    """
    Retourne une nouvelle liste qui contient tous les éléments de L1 qui ne sont pas dans L2.
    """
    result = []
    for element in L1:
        if element not in L2:
            result.append(element)
    return result
