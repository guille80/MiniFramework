class Reverser:
    """Plugin para invertir texto."""

    # name = "reverse"
    # version = "1.0.0"
    # description = "Invierte el texto proporcionado."    
    # @staticmethod

    def __init__(self, data=""):
        self.data = data

    def reverser(self, text: str) -> str:
        return text[::-1]

    def run(self, data) -> str:
        return reverse_text(data)

def reverse_text(text: str) -> str:
    """Invierte un texto."""
    return text[::-1]