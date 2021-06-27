
"""
Implementation des polynomes en python
ROSA Mathias
SCHLÖGEL Benjamin
"""

from fractions import Fract

def deg(expr):
    """
    Prend en argument une expression (str) et renvoie le degré du
    polynome associé à cette expression (convert).
    """
    if expr == "0":
        return "-∞"
    deglist = []
    for i, char in enumerate(expr):
        if char == "X":
            if (i+1) < len(expr) and expr[i + 1] == "^":
                deglist.append(convert("".join(expr[i+2:])))
            else:
                deglist.append(1)
    if deglist != []:
        deglist.sort()
        return deglist[0]
    return 0


def convert(nombre):
    """
    Convertit une chaine de caractères ou un nombre en int ou en float

    Argument
    --------
        nombre : int, float, Fract ou str

    Renvoie
        nombre : int ou float

    """
    if isinstance(nombre, str) and "Fract" in nombre:
        nombre = nombre.split()[0].replace("Fract", "").replace("(", "").replace(")", "").split(",")
        return Fract(*[int(n) for n in nombre])

    if isinstance(nombre, str) and "/" in nombre:
        nombre = nombre.split("/")
        return Fract(*[int(n) for n in nombre])

    nombre = float(nombre)
    if int(nombre) == nombre:
        return int(nombre)

    return float(nombre)

class Polynome:
    """
    Une classe pour représenter un polynôme

    Attribut
    --------
        expression : str

    Méthodes
    --------
        __add__ :
            addition des polynômes
        __neg__ :
            inverse le signe de chaque monome du polynome
        __sub__ :
            soustraction des polynômes
        __mul__ :
            multiplication des polynomes
        derivee :
            donne le polynome derivé
        primitive :
            donne la primitive qui s'annule en 0
        __repr__ :
            représentation du polynome
    """

    def __add__(self, polynome):
        expression_finale = []
        self_expr_copie = self.expr_list[:]
        polynome_expr_copie = polynome.expr_list[:]
        for mono1 in self.expr_list:
            for mono2 in polynome.expr_list:
                if deg(mono1) == deg(mono2):
                    if deg(mono1) in (0, "-∞"):
                        nouveau_monome = f'{convert(mono1.split("X")[0]) + convert(mono2.split("X")[0])}'
                        self_expr_copie.remove(mono1)
                        polynome_expr_copie.remove(mono2)
                    elif deg(mono1) == 1:
                        nouveau_monome = f'{convert(mono1.split("X")[0]) + convert(mono2.split("X")[0])}X'
                        self_expr_copie.remove(mono1)
                        polynome_expr_copie.remove(mono2)
                    else:
                        nouveau_monome = f'{convert(mono1.split("X")[0]) + convert(mono2.split("X")[0])}X^{deg(mono1)}'
                        self_expr_copie.remove(mono1)
                        polynome_expr_copie.remove(mono2)
                    expression_finale.append(nouveau_monome)
        for mono1 in self_expr_copie:
            expression_finale.append(mono1)
        for mono2_restant in polynome_expr_copie:
            expression_finale.append(mono2_restant)
        if "0" in expression_finale and expression_finale != ["0"]:
            expression_finale.remove("0")
        return Polynome("+".join(expression_finale))

    def __neg__(self):
        expression_finale = []
        for monome in self.expr_list:
            if not "-" in monome:
                expression_finale.append("-" + monome)
            else:
                expression_finale.append(monome[1:])
        return Polynome("+".join(expression_finale))

    def __sub__(self, polynome):
        return self + polynome.__neg__()

    def __mul__(self, autre):
        if isinstance(autre, Polynome):
            expression_presque_finale = []
            for mono1 in self.expr_list:
                for mono2 in autre.expr_list:
                    if "-∞" in (deg(mono1), deg(mono2)):
                        nouveau_monome = "0"
                    elif deg(mono1) + deg(mono2) == 0:
                        nouveau_monome = f'{convert(mono1.split("X")[0]) * convert(mono2.split("X")[0])}'
                    elif deg(mono1) + deg(mono2) == 1:
                        nouveau_monome = f'{convert(mono1.split("X")[0]) * convert(mono2.split("X")[0])}X'
                    else:
                        nouveau_monome = f'{convert(mono1.split("X")[0]) * convert(mono2.split("X")[0])}X^{deg(mono1)+deg(mono2)}'
                    expression_presque_finale.append(Polynome(nouveau_monome))
            polynome_final = Polynome("0")
            for monome in expression_presque_finale:
                polynome_final += monome
            return polynome_final

        if isinstance(autre, int):
            expression_finale = []
            for monome in self.expr_list:
                coef = monome.split("X")[0]
                if coef == "":
                    coef = 1
                expression_finale.append(f'{convert(coef) * autre}X^{deg(monome)}')
            return Polynome("+".join(expression_finale))
    
    def __rmul__(self, autre):
            return self * autre

    def __floordiv__(self, autre): # ne marche pas encore
        if self.deg < autre.deg:
            return Polynome("0")
        reste = self
        quotient = Polynome("0")
        if self.deg == autre.deg:
            return Polynome("1")
        while reste.deg >= autre.deg:
            reste = reste - autre
        return reste

    def derivee(self):
        """
        Calcule la dérivée du polynôme
        """
        expression_finale = []
        if self.deg in ("-∞", 0):
            return Polynome("0")
        for mono in self.expr_list:
            if deg(mono) not in ("-∞", 0):
                monolist = mono.split("X")
                if monolist[0] == "":
                    monolist[0] = "1"
                if deg(mono) == 1:
                    nouveau_monome =  f'{convert(monolist[0]) * deg(mono)}'
                elif deg(mono) == 2:
                    nouveau_monome =  f'{convert(monolist[0]) * deg(mono)}X'
                else:
                    nouveau_monome =  f'{convert(monolist[0]) * deg(mono)}X^{deg(mono) - 1}'
                expression_finale.append(nouveau_monome)
        return Polynome("+".join(expression_finale))

    def primitive(self):
        """
        Calcule la primitive du polynôme
        """
        expression_finale = []
        if self.deg in ("-∞", 0):
            return Polynome("1")
        for mono in self.expr_list:
            if deg(mono) != "-∞":
                monolist = mono.split("X")
                if monolist[0] == "":
                    monolist[0] = "1"
                if deg(mono) == 0:
                    nouveau_monome = f'{convert(monolist[0])}X'
                else:
                    nouveau_monome = f'{Fract(convert(monolist[0]), convert(deg(mono)+1))}X^{deg(mono) + 1}'
                expression_finale.append(nouveau_monome)
        return Polynome("+".join(expression_finale))

    def __repr__(self):
        """
        Permet d'afficher le Polynome
        """
        return f'{self.expr}'

    def __init__(self, expr):
        expr_list = expr.replace(" ", "").replace("-", "+-").split("+")
        expr_list = [valeur for valeur in expr_list if valeur != ""]
        for i, nombre in enumerate(expr_list):
            if "Fract" in nombre:
                tartiflette = nombre.split("X") #  On a plus d'inspi mdr
                nombre = tartiflette[0].replace("Fract", "").replace("(", "").replace(")", "").split(",")
                expr_list[i] = f'{Fract(*[int(n) for n in nombre])}X{tartiflette[1]}'
            expr_list[i] = nombre.replace("X^0", "").replace("X^1", "X")
        if "0" not in expr_list:
            expr_list.sort(key=deg, reverse=True)
        self.deg = deg(expr_list[0])
        self.expr_list = expr_list
        self.expr = " + ".join(expr_list).replace("+ -", "- ")
