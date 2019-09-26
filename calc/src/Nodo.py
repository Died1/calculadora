class Nodo:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def esHoja(self):
        return self.left == None and self.right == None
