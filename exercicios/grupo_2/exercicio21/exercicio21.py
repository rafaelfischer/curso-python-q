# Objetivo do programa: Permissão para Dirigir: Uma pessoa pode dirigir se tiver 18 anos ou mais E possuir CNH.
#                      Peça a idade e se possui CNH (sim/não) e informe se a pessoa pode ou não dirigir.
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Verificação de Permissão para Dirigir')
print('------------------------------------')

idade = int(input('Digite sua idade: '))

# Menor de 18 anos
if idade < 18:
    print('Você não pode dirigir')
else:
    tem_cnh = input('Possui CNH? (sim/não): ').lower()
    
    # Validação da resposta
    if tem_cnh not in ['sim', 's', 'não', 'nao', 'n']:
        print('Resposta inválida. Por favor, responda com "sim" ou "não".')
    elif tem_cnh in ['não', 'nao', 'n']:
        print('Você não pode dirigir')
    else:
        print('Você pode dirigir')