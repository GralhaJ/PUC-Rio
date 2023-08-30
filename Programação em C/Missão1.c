#include <stdio.h>

int main(void) {
	int x = 5, y, * p;
	p = &y;
	(*p) = 2;
	printf("Endereco de x em hexadecimal: %x\n", &x);
	printf("Endereco de x em decimal: %d\n", &x);
	printf("Endereco de y em hexadecimal: %x\n", &y);
	printf("Endereco de y em decimal: %d\n", &y);
	printf("Endereco de p em hexadecimal: %x\n", p);
	printf("Endereco de p em decimal: %d\n", p);
	printf("Conteudo de x: %d\n", x);
	printf("Conteudo de y: %d\n", y);
	printf("Conteudo de p: %p\n", p);
	printf("Conteudo de y apontado pelo ponteiro p: %d\n", *p);
	p = p + 1;
	printf("Novo endereco de p em hexadecimal: %p\n", p);
	printf("Novo endereco de p em decimal: %d", p);


}