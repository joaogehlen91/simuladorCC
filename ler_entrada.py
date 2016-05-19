from estrutura import *

def abrir_arquivo(nome_arq):
    return open(nome_arq, 'r')


def ler_arquivo():
    arq  = abrir_arquivo("exemplo_4.in")   
    conf = []

    for i in arq:
        if '*' in i: break

        a = i.split(';')[:-1]
        if a != []: conf.append(a)

    for i in conf:
        print(i)

    #while 'E' not in rea :
    #   rea = arq.read()
    #   print(rea)


#open("exemplo_1.in", "r")

#texto = arq.read()

#lista = texto.replace("\n", "").split(";")

#print (lista)

if __name__ == "__main__":
    ler_arquivo()
