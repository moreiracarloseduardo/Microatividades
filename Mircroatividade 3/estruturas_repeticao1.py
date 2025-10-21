# Microatividade 3: Estrutura de repetição while em Python

# variável entrada_idade
entrada_idade = ''

# Loop while que continua até o usuário digitar 0
while str(entrada_idade) != '0':
    entrada_idade = input('Digite um número qualquer ou 0 para sair: ')
    print('Número digitado: ' + str(entrada_idade))

