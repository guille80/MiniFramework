class Potencia:
    def __init__(self, data=None):
        self.base = 0
        self.exponente = 0
        if data is not None:
            self.exponente = data[1]
            self.base = data[0]
    
    # def calcular(self, base, exponente):
    #     if self.data is not None:
    #         base = self.data[0]
    #         exponente = self.data[1]
    #         # base, exponente = self.data
    #     return base ** exponente
    
    def calcular(self, data=None):
        if data is not None:
            self.base, self.exponente = data
        else:
            raise ValueError("No data provided")
        return self.base ** self.exponente
    
    def run(self, data=None):
        # if data is not None:
        #     self.base, self.exponente = data
        # else:
        #     raise ValueError("No data provided")
        # base, exponente = self.data
        return self.calcular(data)

def doble(x):
    return x * 2