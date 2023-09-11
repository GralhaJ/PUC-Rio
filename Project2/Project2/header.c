#include <stdio.h>

int ler_resp_valida(int questao) {
	int resposta;
	printf("Questao %d - Digite sua opcao de resposta de 1 a 5: ", questao);
	scanf("%d", &resposta);
	while (resposta < 1 || resposta>5) {
		printf("Opcao Invalida. Digite novamente sua resposta: ");
		scanf("%d", &resposta);
	}
	return resposta;
}

int corrige(int* questao, int *gabarito) {
	int i, contador = 0;
	for (i = 0; i < 10; i++) {
		if (questao[i] == gabarito[i]) {
			contador++;
		}
	}
	return contador;
}