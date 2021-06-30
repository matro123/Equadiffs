#! /usr/bin/env python3
# coding: utf-8
"""
Potentiellement un solveur d'équations différentielles
ROSA Mathias
ROURE Mathéo
SCHLÖGEL Benjamin
"""

from polynomes import Polynome
from fractions import Fract

class Diff:
    # diff("2y' + 3y = 0")

    def normaliser(self):
        pass

    def equation_homogene(self):
        # si polynome, on primitive, sinon regarder dans le dictionnaire poir plus tard
        pass
    
    def __init__(self, expr):
        self.expr = expr


# dictionnaire des primitives connues
primitives = {
    "exp" : "exp"
}


"""Ici, Prochainement un solveur d'équations différentielles"""
