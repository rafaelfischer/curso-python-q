# Objetivo do programa: Validação de Data: Crie um algoritmo que verifique se uma data (dia, mês, ano) é válida.
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

def validar_data(dia, mes, ano):
    if mes < 1 or mes > 12 or dia < 1:
        return False
    
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes == 2 and ((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0):
        dias_por_mes[2] = 29
    
    return dia <= dias_por_mes[mes]

print('Validação de Data')
print('----------------')

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

data_valida = validar_data(dia, mes, ano)
print('Data válida' if data_valida else 'Data inválida')