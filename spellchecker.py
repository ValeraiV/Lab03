import time
import multiDictionary as md
mdic = md.MultiDictionary()
a = []
class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        txt = replaceChars(txtIn).split()
        b = "resources/"+language.capitalize()+".txt"
        for i in mdic.searchWord(txt, b):
            print (i)


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\'*_{}><#+-.!$£%&^;,=-§"
    for c in chars:
        text = text.replace(c, "")
    return text