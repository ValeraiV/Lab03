import dictionary as d
import richWord as rw
dic = d.Dictionary()

dizionario = []

class MultiDictionary:

    def __init__(self):
        self.dizionario = dic

    def printDic(self, language):
        dic.loadDictionary(language)

    def searchWord(self, words, language):
        dic.loadDictionary(language)
        lista = []
        for i in words:
            rword = rw.RichWord(i).corretta
            if rword == False:
                lista.append(i)
        return lista

    def searchWordLinear(self, words, language):
        dic.loadDictionary(language)
        lista_errate = []
        diz = dic.dict.copy()
        for i in words:
            parola = False
            for j in diz:
                if j == i:
                    parola = True
            if parola == False:
                lista_errate.append(i)
        return lista_errate

    def searchWordDichotomic(self, words, language):
        dic.loadDictionary(language)
        lista_errate = []

        for i in words:
            lista_parole = dic.dict.copy()
            while len(lista_parole) != 0:
                mid_index = int(len(lista_parole)/2)
                if i<lista_parole[mid_index]:
                    del lista_parole[mid_index:]
                elif i>lista_parole[mid_index]:
                    del lista_parole[:mid_index]
                elif i==lista_parole[mid_index]:
                    lista_parole.clear()

                if len(lista_parole)==1:
                    if lista_parole[0]!=i:
                        lista_errate.append(i)
                    lista_parole.pop(0)
        return lista_errate