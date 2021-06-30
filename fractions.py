#! /usr/bin/env python3
# coding: utf-8
"""
Implementation des fractions en python
ROSA Mathias
ROURE Mathéo
SCHLÖGEL Benjamin
"""

def euclide_pgcd(numerateur, denominateur):
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

    return euclide_pgcd(denominateur, numerateur % denominateur)


def simp(numerateur, denominateur):
    """
    Simplifie une fraction (instance de la classe Fract)

    Argument
    --------
        numerateur : int
        denominateur : int

    Renvoie
        fraction simplifiée : Instance de la classe Fract

    Note : Une fraction est automatiquement simplifiée. (ne sert à rien)
    """
    if numerateur % denominateur == 0:
        return int(numerateur / denominateur)

    return Fract(int(numerateur / euclide_pgcd(numerateur, denominateur)),
                 int(denominateur / euclide_pgcd(numerateur, denominateur)))


class Fract:
    """
    Une classe pour représenter une fraction

    Attributs
    ---------
        numerateur : int
        denominateur : int

    Méthodes
    --------
        int_convert :
            convertit une fraction en int si son denominateur est égal à 1
        __mul__ :
            multiplication de fractions
        __add__ :
            addition des fractions
        __neg__ :
            inverse d'une fraction par rapport à la multiplication (multiplie par -1)
        __sub__ :
            soustraction des fractions
        __truediv__ :
            division des fractions
        __mod__ :
            renvoie le reste de la division euclidienne de deux fractions
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
        return Fract(self, autre)

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
            nouveau_numerateur = numerateur.numerateur * denominateur.denominateur
            nouveau_denominateur = numerateur.denominateur * denominateur.numerateur
        elif isinstance(numerateur, Fract):
            nouveau_numerateur = numerateur.numerateur
            nouveau_denominateur = numerateur.denominateur * denominateur
        elif isinstance(denominateur, Fract):
            nouveau_numerateur = numerateur * denominateur.denominateur
            nouveau_denominateur = denominateur.numerateur
        else:
            nouveau_numerateur, nouveau_denominateur = numerateur, denominateur
        if nouveau_numerateur < 0 and nouveau_denominateur < 0:
            nouveau_numerateur = -nouveau_numerateur
            nouveau_denominateur = -nouveau_denominateur
        self.numerateur = int(nouveau_numerateur / euclide_pgcd(nouveau_numerateur, nouveau_denominateur))
        self.denominateur = int(nouveau_denominateur / euclide_pgcd(nouveau_numerateur, nouveau_denominateur))
