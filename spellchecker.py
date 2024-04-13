import time
import multiDictionary as md
mdic = md.MultiDictionary()
a = []
class SpellChecker:

    def __init__(self):
        self.a = a

    def handleSentence(self, txtIn, language):
        txt = replaceChars(txtIn).split()
        b = "resources/"+language.capitalize()+".txt"

        start_time = time.time()
        ricerca = mdic.searchWord(txt, b)
        end_time = time.time()
        print("______________________________\nUsing contains:")
        for i in ricerca:
            print(i)
        print("Time elapsed "+str(end_time - start_time)+
              "\n______________________________\n")

        start_time = time.time()
        ricerca_lineare = mdic.searchWordLinear(txt, b)
        end_time = time.time()
        print("Using Linear search:")
        for i in ricerca_lineare:
            print(i)
        print("Time elapsed " + str(end_time - start_time) +
              "\n______________________________\n")

        start_time = time.time()
        ricerca_dicotomica = mdic.searchWordDichotomic(txt, b)
        end_time = time.time()
        print("Using Dichotomic search:")
        for i in ricerca_dicotomica:
            print(i)
        print("Time elapsed " + str(end_time - start_time))





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