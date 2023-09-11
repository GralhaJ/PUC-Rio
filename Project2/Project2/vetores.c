#include <stdio.h>
#include "header.h"

int main(void) {

	/*
	 vetor é um ponteiro constante.
	 vGab guarda um endereço mas uma vez estabelecido, ele não muda.
	 se printar o vGab ele irá indicar o endereço da primeira célula.
	 printf("%p", vGab);
	*/

	int i, vGab[10] = {1,2,1,3,5,5,4,4,3,2}, vResp[10];
	for (i = 0; i < 10; i++) {
		vResp[i] = ler_resp_valida(i + 1);
		
	}
	for (i = 0; i < 10; i++) {
		printf("Q%d: %d\n", i + 1, vGab[i]);
	}

	printf("Total de Acertos: %d", corrige(vResp, vGab));

	return 0;
}