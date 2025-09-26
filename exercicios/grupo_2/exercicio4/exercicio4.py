# Objetivo do programa: Pergunte a data de nascimento e verifique se a data atual é a data de aniversário.
#                      Se for, printe a mensagem de Feliz Aniversário, senão printe a mensagem hoje e dia X de Y
#                      de ZZZZ.
# Data da criacao: 2025-09-23
# Criado por: @rafaelfischer

from datetime import datetime

print('Verificação de Aniversário')
print('--------------------------')

# Solicita a data de nascimento
dia_nascimento = int(input('Digite o dia do seu nascimento: '))
mes_nascimento = int(input('Digite o mes do seu nascimento: '))

# Obtém a data atual
hoje = datetime.now()
dia_atual = hoje.day
mes_atual = hoje.month
ano_atual = hoje.year

# Obtém o nome do mês atual
nome_mes_atual = hoje.strftime('%B')

# Verifica se é aniversário
if dia_nascimento == dia_atual and mes_nascimento == mes_atual:
    print('Feliz Aniversário!')
else:
    print(f'Hoje é dia {dia_atual} de {nome_mes_atual} de {ano_atual}')