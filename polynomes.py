
"""
Implementation des polynomes en python
ROSA Mathias
SCHLÖGEL Benjamin
"""

def deg(expr):
    """
    Prend en argument une expression (str) et renvoie le degré du
    polynome associé à cette expression (int_ou_float).
    """
    if expr == "0":
        return "-∞"
    deglist = []
    for i, char in enumerate(expr):
        if char == "X":
            if (i+1) < len(expr) and expr[i + 1] == "^":
                deglist.append(int_ou_float("".join(expr[i+2:])))
            else:
                deglist.append(1)
    if deglist != []:
        deglist.sort()
        return deglist[0]
    return 0


def int_ou_float(nombre):
    """
    Convertit une chaine de caractères ou un nombre en int ou en float

    Argument
    --------
        nombre : int, float ou str

    Renvoie
        nombre : int ou float

    """
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
        __sub__ :
            soustraction des polynômes
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
                        nouveau_monome = f'{int_ou_float(mono1.split("X")[0]) + int_ou_float(mono2.split("X")[0])}'
                        self_expr_copie.remove(mono1)
                        polynome_expr_copie.remove(mono2)
                    elif deg(mono1) == 1:
                        nouveau_monome = f'{int_ou_float(mono1.split("X")[0]) + int_ou_float(mono2.split("X")[0])}X'
                        self_expr_copie.remove(mono1)
                        polynome_expr_copie.remove(mono2)
                    else:
                        nouveau_monome = f'{int_ou_float(mono1.split("X")[0]) + int_ou_float(mono2.split("X")[0])}X^{deg(mono1)}'
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

    def __sub__(self, polynome):
        expression_finale = []
        self_expr_copie = self.expr_list[:]
        polynome_expr_copie = polynome.expr_list[:]
        for mono1 in self.expr_list:
            for mono2 in polynome.expr_list:
                if deg(mono1) == deg(mono2):
                    if deg(mono1) == 0:
                        nouveau_monome = f'{int_ou_float(mono1.split("X")[0]) - int_ou_float(mono2.split("X")[0])}'
                        self_expr_copie.remove(mono1)
                        polynome_expr_copie.remove(mono2)
                    elif deg(mono1) == 1:
                        nouveau_monome = f'{int_ou_float(mono1.split("X")[0]) - int_ou_float(mono2.split("X")[0])}X'
                        self_expr_copie.remove(mono1)
                        polynome_expr_copie.remove(mono2)
                    else:
                        nouveau_monome = f'{int_ou_float(mono1.split("X")[0]) - int_ou_float(mono2.split("X")[0])}X^{deg(mono1)}'
                        self_expr_copie.remove(mono1)
                        polynome_expr_copie.remove(mono2)
                    expression_finale.append(nouveau_monome)
        for mono1 in self_expr_copie:
            expression_finale.append(mono1)
        for mono2 in polynome_expr_copie[:-1]:
            expression_finale.append("-" + mono2)
        return Polynome("+".join(expression_finale))

    def __mul__(self, polynome):
        expression_presque_finale = []
        for mono1 in self.expr_list:
            for mono2 in polynome.expr_list:
                if "-∞" in (deg(mono1), deg(mono2)):
                    nouveau_monome = "0"
                elif deg(mono1) + deg(mono2) == 0:
                    nouveau_monome = f'{int_ou_float(mono1.split("X")[0]) * int_ou_float(mono2.split("X")[0])}'
                elif deg(mono1) + deg(mono2) == 1:
                    nouveau_monome = f'{int_ou_float(mono1.split("X")[0]) * int_ou_float(mono2.split("X")[0])}X'
                else:
                    nouveau_monome = f'{int_ou_float(mono1.split("X")[0]) * int_ou_float(mono2.split("X")[0])}X^{deg(mono1)+deg(mono2)}'
                expression_presque_finale.append(Polynome(nouveau_monome))
        polynome_final = Polynome("0")
        for monome in expression_presque_finale:
            polynome_final += monome
        return polynome_final

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
                    nouveau_monome =  f'{int_ou_float(monolist[0]) * deg(mono)}'
                elif deg(mono) == 2:
                    nouveau_monome =  f'{int_ou_float(monolist[0]) * deg(mono)}X'
                else:
                    nouveau_monome =  f'{int_ou_float(monolist[0]) * deg(mono)}X^{deg(mono) - 1}'
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
                    nouveau_monome = f'{int_ou_float(monolist[0])}X'
                else:
                    nouveau_monome = f'{int_ou_float(monolist[0]) / (deg(mono)+1)}X^{deg(mono) + 1}'
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
        if "0" not in expr_list:
            expr_list.sort(key=deg, reverse=True)
        self.deg = deg(expr_list[0])
        self.expr_list = expr_list
        self.expr = " + ".join(expr_list).replace("+ -", "- ")
