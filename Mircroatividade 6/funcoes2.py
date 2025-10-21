# Microatividade 6: Utilização de argumentos de funções no Python

# função loginUsuario
def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# função com diferentes valores
print('Teste 1:')
loginUsuario('Admin')

print('\nTeste 2:')
loginUsuario('admin')

print('\nTeste 3:')
loginUsuario('User')

print('\nTeste 4:')
loginUsuario('usuário')

print('\nTeste 5:')
loginUsuario('ADMIN')
