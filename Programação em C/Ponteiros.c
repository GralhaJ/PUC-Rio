#include <stdio.h>

int main(void) {
	int i1 = 1, i2 = 2, *pi;
	float f1 = 1.2, f2 = 2.5, *pf;
	char c1 = 'a', c2 = 'b', * pc;
	
	printf("O valor de i1 e i2 antes da modificacao sao, respectivamente: %d e %d\n", i1, i2);
	printf("O valor de f1 e f2 antes da modificacao sao, respectivamente: %.2f e %.2f\n", f1, f2);
	printf("O valor de c1 e c2 antes da modificacao sao, respectivamente: %c e %c\n", c1, c2);

	pi = &i1;
	*pi = *pi + 1;
	pi = &i2;
	*pi = *pi + 1;

	pf = &f1;
	*pf = *pf + 1;
	pf = &f2;
	*pf = *pf + 1;

	pc = &c1;
	*pc = *pc + 1;
	pc = &c2;
	*pc = *pc + 1;

	printf("O valor de i1 e i2 depois da modificacao sao, respectivamente: %d e %d\n", i1, i2);
	printf("O valor de f1 e f2 depois da modificacao sao, respectivamente: %.2f e %.2f\n", f1, f2);
	printf("O valor de c1 e c2 depois da modificacao sao, respectivamente: %c e %c\n", c1, c2);

	return 0;
}