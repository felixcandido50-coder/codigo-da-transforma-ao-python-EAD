'''




'''


int main() {
    int idade;
    
    printf("Digite a sua idade: ");
    scanf("%d", &idade);
    
    if (idade < 12) {
        printf("Crianca\n");
    } else if (idade < 18) {
        printf("Adolescente\n");
    } else if (idade < 60) {
        printf("Adulto\n");
    } else {
        printf("Idoso\n");
    }
    
    return 0;
}