#include <stdio.h>
#define TAM 13

void exibe_vetor(int vet[]) {
	int i;
	printf("\n============================================\n");
	for (i = 0; i < TAM; i++) {
		printf("\npos: %d\tval: %d", i, vet[i]);
	}
	printf("\n============================================\n");
	return;
}
int preenche_vazio_ord(int vA[], int tam_vA, int vB[], int tam_vB, int vVazio[]) 
{
	int i = 0, k = 0, pos = 0;
	for (i = 0; i < tam_vA; i++) 
	{
		for (k = 0; k <tam_vB; k++)
		{
			if (vA[i] == vB[k]) 
			{
				vVazio[pos] = vA[i];
				pos++;
			}
		}
	}
	return pos;
}
/*int preenche_vazio_desord(int vA[], int vB[], int vVazio[])
{

}*/

int main(void)
{
	int tam_inter_Ord;
	int vet[TAM] = { 11,10,13,12,14,20,24,16,15,19,17,18,10 };
	int A_Ord[7] = { 1,10, 16, 17, 18, 20,28 };
	int B_Ord[TAM-1] = { 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 24 };
	int inter_Ord[TAM];
	/*int A_Desord[7] = {1,28,18, 20, 11, 24, 13};
	int B_Desord[TAM-1] = { 12, 18, 13, 14, 19, 15, 17, 16, 20, 11, 24, 10 };
	int uniao_Ord[2 * TAM];
	int uniao_Desord[2 * TAM];
	int inter_Desord[TAM];
	int diferenca_Ord[TAM];
	int diferenca_Desord[TAM];*/
	int tam_vA = sizeof(A_Ord) / sizeof(int);
	int tam_vB = sizeof(B_Ord) / sizeof(int);
	//exibe_vetor(vet);
	//printf("\nHa %d numero %d", conta_vetor(vet), vet[TAM - 1]);
	tam_inter_Ord = preenche_vazio_ord(A_Ord, tam_vA, B_Ord, tam_vB, inter_Ord);
	printf("%d", tam_inter_Ord);
	return 0;
}

