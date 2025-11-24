class Reductor:
    def __init__(self, data=None):
        self.total = 0
        if data is not None:
            for valor in data:
                self.reducir(valor)

    def reducir(self, valor):
        self.total -= valor

    def obtener_total(self):
        return self.total
    
    def run(self, data):
        for valor in data:
            self.reducir(valor)
        return self.obtener_total()
    
def resta(a, b):
    """
    Resta dos números.

    Parámetros:
    a -- El primer número.
    b -- El segundo número.

    Retorna:
    La resta de a y b.
    """
    return a - b