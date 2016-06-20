import ler_entrada as le
import definicoes  as df 

def infinitos_servidores():
   print(df.TS, df.TC)


if __name__ == '__main__':
   le.ler_arquivo("exemplo_4.in")
   infinitos_servidores()