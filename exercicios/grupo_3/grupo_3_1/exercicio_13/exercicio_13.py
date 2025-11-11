"""
Grupo 3.2
Exercício: 13
Metodo: Simplificado
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Verificar Caracteres Específicos em Frase: Receba uma frase do usuário. 
	Use um loop para iterar sobre a frase e conte quantos caracteres são vogais (a, e, i, o, u, maiúsculas ou minúsculas) OU são dígitos numéricos (0-9).
"""

def contar_vogais_e_digitos(frase: str) -> int:
    """
    Conta quantos caracteres da frase são vogais (a, e, i, o, u, maiúsculas ou minúsculas)
    ou dígitos numéricos (0-9).
    """
    vogais = "aeiouAEIOU"
    digitos = "0123456789"
    contador = 0

    # Percorre cada caractere da frase
    for caractere in frase:
        if caractere in vogais or caractere in digitos:
            contador += 1

    return contador


def main():
    # Solicita a frase ao usuário
    frase_usuario = input("Digite uma frase: ")

    # Conta vogais e dígitos
    total = contar_vogais_e_digitos(frase_usuario)

    # Exibe o resultado
    print(f"Total de vogais ou dígitos encontrados: {total}")


# Executa o programa apenas se este arquivo for executado diretamente
if __name__ == "__main__":
    main()
