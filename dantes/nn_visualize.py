from .io import cardstr, print_deal


def icard(i):
    return (i % 13, i // 13)


def print_linear_significant_card(coeffs):
    tableau = []
    for i in range(52):
        i = coeffs[i*52:(i+1)*52].argmax()
        tableau.append(icard(i))
    print_deal(tableau)
