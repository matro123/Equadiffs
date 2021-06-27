
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

    def int_convert(self):
        if self.denominateur == 1:
            return self.numerateur
        return self

    def __mul__(self, autre):
        if isinstance(autre, int):
            autre = Fract(autre, 1)
        return Fract(self.numerateur * autre.numerateur,
                     self.denominateur * autre.denominateur).int_convert()

    def __rmul__(self, autre):
        return self * autre

    def __add__(self, autre):
        if isinstance(autre, int) or isinstance(autre, float):
            autre = Fract(autre, 1)
        return Fract(self.numerateur * autre.denominateur + autre.numerateur * self.denominateur,
                     self.denominateur * autre.denominateur).int_convert()

    def __radd__(self, autre):
        return self + autre

    def __neg__(self):
        return -1 * self

    def __sub__(self, autre):
        return self + autre.__neg__()

    def __rsub__(self, autre):
        return self.__neg__() + autre

    def __truediv__(self, autre):
        if isinstance(autre, int):
            return Fract(self.numerateur, (self.denominateur * autre))

        nouveau_num = (self.numerateur * autre.denominateur)
        nouveau_den = (self.denominateur * autre.numerateur)
        return Fract(int(nouveau_num / euclide_PGCD(nouveau_num, nouveau_den)), int(nouveau_den / euclide_PGCD(nouveau_num, nouveau_den)))

    def __rtruediv__(self, autre):
        autre_fraction = Fract(autre,1)
        return autre_fraction / self

    def __mod__(self, autre):
        fraction_simplifiee = self / autre
        return fraction_simplifiee.numerateur % fraction_simplifiee.denominateur

    def __rmod__(self, autre):
        autre_fraction = Fract(autre,1)
        return autre_fraction % self

    def __repr__(self):
        # Le if c'est pour faire joli
        if self.denominateur == 1:
            return f'{self.numerateur}'
        return f'{self.numerateur}/{self.denominateur}'

    def __init__(self, numerateur, denominateur):
        if isinstance(numerateur, Fract) and isinstance(denominateur, Fract):
            # numerateur et denominateur sont des objets Fract
            self.numerateur = numerateur.numerateur * denominateur.denominateur
            self.denominateur = numerateur.denominateur * denominateur.numerateur
        elif isinstance(numerateur, Fract):
            self.numerateur = numerateur.numerateur
            self.denominateur = numerateur.denominateur * denominateur
        elif isinstance(denominateur, Fract):
            self.numerateur = numerateur * denominateur.denominateur
            self.denominateur = denominateur.numerateur
        else:
            self.numerateur = int(numerateur / euclide_PGCD(numerateur, denominateur))
            self.denominateur = int(denominateur / euclide_PGCD(numerateur, denominateur))
        if self.numerateur < 0 and self.denominateur < 0:
            self.numerateur = -self.numerateur
            self.denominateur = -self.denominateur

