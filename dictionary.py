_dict = []

class Dictionary:
    def __init__(self):
        self._dict = _dict

    def loadDictionary(self,path):
        with open(path, "r", encoding="utf-8") as file:
            carattere= "/"
            for parola in file:
                stringa = parola.rstrip("\n").lower()
                indice = parola.find(carattere)
                if indice != -1:
                    stringa = parola[:indice]
                if stringa.isalpha():
                    _dict.append(stringa)
        sorted(_dict)


    def printAll(self):
        for i in _dict:
            print(i)


    @property
    def dict(self):
        return self._dict