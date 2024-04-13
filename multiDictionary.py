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
        diz = dic.dict
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
            start = 0
            end = len(dic.dict)
            parola = False

            while (start != end) and parola != True:
                media = start + int((end - start) / 2)
                parola_corrente = dic.dict[media]
                if i == parola_corrente:
                    parola = True
                elif i > parola_corrente:  # in python < applied to strings gives True if the first string is before in lexicographic order
                    start = media + 1
                else:
                    end = media

            if parola == False:
                lista_errate.append(i)

        return lista_errate