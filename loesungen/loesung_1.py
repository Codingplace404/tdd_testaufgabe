from numbers import Real


def division(a: Real, b: Real) -> Real:
    """
    Dividiert zwei zahlen a und b und rundet Ergebnis automatisch auf 4
    Nachkommastellen

    :param a: Zaehler, kann float oder int sein.
    :param b: Nenner, kann float oder int sein.
    :returns: division a / b gerundet auf 4 nachkommastellen
              None wenn a oder b string ist
              None wenn b = 0
    """
    if not isinstance(a, Real) or not isinstance(b, Real) or b == 0:
        return None

    return round(a/b, 4)
