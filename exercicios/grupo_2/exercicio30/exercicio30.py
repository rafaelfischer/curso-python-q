# Objetivo do programa: Aceitar Convite: Um convite será aceito se a pessoa for "amigo" OU for "familia" E estiver disponível
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Sistema de Convites')
print('-----------------')

relacao = input('Qual o tipo de relação? (amigo/familia): ').lower()
disponivel = input('Está disponível? (sim/não): ').lower()

aceito = relacao == 'amigo' or (relacao == 'familia' and disponivel == 'sim')

print('Convite aceito' if aceito else 'Convite não aceito')