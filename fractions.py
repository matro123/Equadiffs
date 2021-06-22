
"""
Implementation des fractions en python
ROSA Mathias
SCHLÖGEL Benjamin
"""


def euclide_PGCD(numerateur, denominateur):
    """
    Donne le PGCD de deux nombres grêce à l'algorithme d'euclide et la
    récursivité

    Argument
    --------
        numerateur : int
        denominateur : int

    Renvoie
        pgcd : int

    """
    if denominateur == 0:
        return numerateur

    return euclide_PGCD(denominateur, numerateur % denominateur)


def simp(numerateur, denominateur):
    """
    Simplifie une fraction (instance de la classe Fract)

    Argument
    --------
        numerateur : int
        denominateur : int

    Renvoie
        fraction simplifiée : Instance de la classe Fract

    """
    if numerateur % denominateur == 0:
        return int(numerateur / denominateur)

    return Fract(int(numerateur / euclide_PGCD(numerateur, denominateur)),
                 int(denominateur / euclide_PGCD(numerateur, denominateur)))


class Fract:
    """
    Une classe pour représenter une fraction

    Attributs
    ---------
        numerateur : int
        denominateur : int

    Méthodes
    --------
        __mul__ :
            multiplication de fractions
        __repr__ :
            représentation de la fraction
    """

    def __mul__(self, autre):
        if isinstance(autre, int):
            autre = Fract(autre, 1)
        return Fract(self.numerateur * autre.numerateur,
                     self.denominateur * autre.denominateur)

    def __rmul__(self, autre):
        return self * autre

    def __add__(self, autre):
        if isinstance(autre, int):
            autre = Fract(autre, 1)
        return Fract(self.numerateur * autre.denominateur + autre.numerateur * self.denominateur,
                     self.denominateur * autre.denominateur)

    def __radd__(self, autre):
        return self + autre

    def __sub__(self, autre):
        return self + -1 * autre

    def __rsub__(self, autre):
        return -1 * self + autre

    def __repr__(self):
        return f'{self.numerateur}/{self.denominateur}'

    def __init__(self, numerateur, denominateur):
        self.numerateur = int(numerateur / euclide_PGCD(numerateur, denominateur))
        self.denominateur = int(denominateur / euclide_PGCD(numerateur, denominateur))
