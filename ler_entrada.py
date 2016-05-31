from estrutura import *

def abrir_arquivo(nome_arq):
    return open(nome_arq, 'r')


def ler_arquivo():
    arq  		= abrir_arquivo("exemplo_4.in")   
    conf 		= []

    for i in arq:
        if '*' in i: break

        a = i.split(';')[:-1]
        if a != []: 
        	b = a[0].split(':')

        	#print("A -> " + str(a))
        	#print("B -> " + str(b))
        	
        	try:
        		#print("C -> " + str(b[1].split(',')))
        		conf.append((b[0], b[1].split(',')))
        	except:
        		pass
        	

    for i,j in conf:
    	for k in j:
    		print(k)
    	print('\n')


if __name__ == "__main__":
    ler_arquivo()
