/* Criacao dos objetos */
E;
C1:1(1 - 4);
C2:1(4 - 8), 2(4 - 8), 3(5 - 9);
I1:1(4 - 8);
S;

R1:(30 - C2), (30 - I1), (30 - C1);
R2:(20 - I1), (80 - S);

*

/* Configuracao dos objetos */
E->C1;
C1->R1;
I1->C2;
C2->R2;

TS=50000

TC:3,5

E - Entrada
C - Componente
I - Infinitos servidores
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

