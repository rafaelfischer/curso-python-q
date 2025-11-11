"""
Grupo 3.2
Exercício: 9
Metodo: Tradicional
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Tentativas de Senha Limitadas: A senha correta é "topsecret". 
    Peça ao usuário para digitar a senha. 
    Ele tem 3 tentativas. 
    Use um loop e condicionais para informar se ele acertou ou se esgotou as tentativas. 
"""
def verificar_senha(senha_correta: str, max_tentativas: int) -> None:
    """
    Solicita senha ao usuário até acertar ou esgotar tentativas.
    """
    for tentativa in range(1, max_tentativas + 1):
        # Pede a senha
        senha_digitada = input("Digite a senha: ")

        # Compara
        if senha_digitada == senha_correta:
            print("Acesso liberado!")
            return

        # Avisa quantas tentativas restam
        restantes = max_tentativas - tentativa
        if restantes > 0:
            print(f"Senha incorreta. Você ainda tem {restantes} tentativa(s).")
        else:
            print("Senha incorreta. Tentativas esgotadas.")

    print("Acesso bloqueado.")


# Constantes do exercício
SENHA_CORRETA = "topsecret"
LIMITE_TENTATIVAS = 3

# Executa o programa
if __name__ == "__main__":
    verificar_senha(SENHA_CORRETA, LIMITE_TENTATIVAS)
