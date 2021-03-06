#! /usr/bin/env python3
# coding: utf-8
"""
Implementation des équations en python
ROSA Mathias
ROURE Mathéo
SCHLÖGEL Benjamin
"""

class Equation:

    # Equa("2x + 3 = 5")

    def __init__(self, expr):
        self.expr = expr
        self.expr_split = expr.split("=")

        # reconnaissance de l'ordre

        if "''" in self.expr_split[0]:
            self.ordre = 2
        elif "'" in self.expr_split[0]:
            self.ordre = 1
        else:
            self.ordre = 0
