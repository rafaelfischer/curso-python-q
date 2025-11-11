"""
Grupo 3.2
Exercício: 5   
Metodo: Tradicional
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Verificar Presença de Vogal: Peça ao usuário para digitar uma palavra. 
    Use um loop para verificar cada letra da palavra e informe se a palavra contém pelo menos uma vogal.
"""

def contem_vogal(palavra: str) -> bool:
    """
    Verifica se a palavra possui ao menos uma vogal.
    """
    vogais = "aeiouAEIOU"
    for letra in palavra:
        if letra in vogais:
            return True
    return False


def main():
    # Solicita palavra ao usuário
    palavra = input("Digite uma palavra: ").strip()

    # Validação simples
    if not palavra:
        print("Você não digitou nada.")
        return

    # Verifica presença de vogal e informa o resultado
    if contem_vogal(palavra):
        print("A palavra contém pelo menos uma vogal.")
    else:
        print("A palavra não contém vogais.")


if __name__ == "__main__":
    main()
