lista = []
class Dictionary:
    def __init__(self):
        self.lista = lista

    def loadDictionary(self,path):
        with open(path, "r") as file:
            for parola in file:
                lista.append(parola.rstrip("\n"))

    def printAll(self):
        pass


    @property
    def dict(self):
        return self.lista