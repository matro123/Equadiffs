
def deg(expr):
    """
    Prend en argument une expression (str) et renvoie le degré du
    polynome associé à cette expression (int).
    """
    if expr == "0":
        return "-∞"
    deglist = []
    for i, e in enumerate(expr):
        if e == "X":
            if (i+1) < len(expr) and expr[i + 1] == "^":
                deglist.append(int(expr[i+2]))
            else:
                deglist.append(1)
    
    if deglist != []:
        deglist.sort()
        return deglist[0]
    return 0

class Polynome:

    def __init__(self, expr):
        expr_list = expr.replace(" ","").replace("-","+-").split("+")
        expr_list.sort(key=deg, reverse=True)
        self.deg = deg(expr_list[0])
        self.expr = " + ".join(expr_list).replace("+ -","- ")

    def __add__(self, polynome):
        return "bonjour"

    def __sub__(self, polynome):
        return "au revoir"

    def __repr__(self):
        """
        Permet d'afficher le Polynome
        """
        return f'{self.expr}'