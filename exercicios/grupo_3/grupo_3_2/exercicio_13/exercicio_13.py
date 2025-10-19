# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Contagem de Caracteres: Receba uma frase do usuário e conte quantas vezes a letra 'a' (maiúscula ou minúscula) aparece na frase.

def contar_letra_a(frase: str) -> int:
    """Conta quantas vezes a letra 'a' (maiúscula ou minúscula) aparece na frase."""
    return frase.lower().count('a')


def main():
    # Pede a frase ao usuário
    frase_usuario = input("Digite uma frase: ")

    # Conta as letras 'a'
    quantidade = contar_letra_a(frase_usuario)

    # Exibe o resultado
    print(f"A letra 'a' aparece {quantidade} vez(es) na frase.")


if __name__ == "__main__":
    main()
