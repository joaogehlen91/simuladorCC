#include<stdio.h>
#include<stdlib.h>
//função que recebe entidade temporária como parametro e devolve atualizada com o tempo de atendimento
int InfinitoSer(int entidadeTemp){
	
	int r;
	r=rand() % 8;						//tempo de atendimento no componente
	entidadeTemp = entidadeTemp + r;	//atualiza entidade temporária
	return entidadeTemp;				//retorna entidade temporária atualizada
}

	
