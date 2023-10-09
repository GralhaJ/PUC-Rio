#include  <stdlib.h>
#include  <stdio.h>


FILE* abreArquivo(char* arquivo, char* modo) {
	FILE* pArq;
	pArq = fopen(arquivo, modo);
	if (pArq == NULL) {
		printf("Erro na abertura do arquivo %s",arquivo);
		exit(1);
	}
	return pArq;
}
int main(void) {
	FILE* pEnt, * pSai;
	int i;
	int matr;
	float nota;
	pEnt = abreArquivo("P:\\INF1037\\notas.txt", "rt");
	pSai = abreArquivo("P:\\INF1037\\provafinal.txt", "wt");
	printf("OK");
	while (fscanf(pEnt, "%d %f", &matr, &nota)==2){
		printf("\nMatr: %d  - Nota: %.2f", matr, nota);
		if (nota <= 6) {
			fprintf(pSai, "%d % .2f\n", matr, nota);
		}
	}
	fclose(pEnt);
	fclose(pSai);

}