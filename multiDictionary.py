import dictionary as d
import richWord as rw
dic = d.Dictionary()

dizionario = []

class MultiDictionary:

    def __init__(self):
        self.dizionario = dic


    def printDic(self, language ):
        dic.loadDictionary(language)


    def searchWord(self, words, language):
        dic.loadDictionary(language)
        lista = []
        for i in words:
            rword = rw.RichWord(i).corretta
            if rword == False:
                lista.append(i)

        return lista



