class Sumatoria:
    def __init__(self, data=None):
        self.total = 0
        if data is not None:
            for valor in data:
                self.agregar(valor)

    def agregar(self, valor):
        self.total += valor

    def obtener_total(self):
        return self.total
    
    def run(self, data):
        for valor in data:
            self.agregar(valor)
        return self.obtener_total()

def suma(a, b):
    """
    Suma dos números y devuelve el resultado.

    Parámetros:
    a (int, float): El primer número.
    b (int, float): El segundo número.

    Retorna:
    int, float: La suma de los dos números.
    """
    return a + b