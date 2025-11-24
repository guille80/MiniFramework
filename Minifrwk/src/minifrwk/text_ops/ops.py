class Text_ops:
    def __init__(self, text=""):
        self.text = text

    def capitalize(self):
        return self.text.capitalize()
    
    def uppercase(self):
        return self.text.upper()
    
    def lowercase(self):
        return self.text.lower()
    
    def run(self, data):
        results = []
        for text in data:
            self.text = text
            results.append(self.uppercase())
        return results