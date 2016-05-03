/* Componente */
C1:1(4,8)
C2:1(7,14), 2(10,15)
CI:S1

/* Roteamento */
R1:(3, C1), (7, S1)

E1->C1
C1->C2
C2->R1
R1->C1, S1

TS=50000

E - Entrada
C - Componente
R - Roteamento
S - Saída

Estrutura básica de cada roteador:
 - Nome
 - Lista de saídas 

Estrutura básica de cada Entidade Temporária:
 - Identificação
 - Tempo Chegada



Estrutura básica de cada componente:
 - Nome
 - Número de Servidores
 - Lista de Servidores
 - Saída
 - Entrada

Estrutura dos Servidores
 - Número
 - Intervalo
 - Ociosidade

