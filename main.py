# usuario inserindo os dados - adicionar

usuario = {}
usuario['Nome'] = input('informe seu nome: ')
usuario['Idade'] = input('informe sua idade: ')
usuario['Sexo'] = input('informe seu sexo: ')
usuario['Estado'] = input('informe seu Estado: ')
usuario['Cidade'] = input('informe seu Cidade: ')
usuario['E-mail'] = input('informe seu e-mail: ')
usuario['CPF'] = input('informe seu CPF: ')
usuario['Mae'] = input('informe o nome da sua mãe: ')
usuario['Pai'] = input('informe o nome do seu pai: ')
usuario['Data de Nascimento'] = input('informe sua data de nascimento: ')

for chave in usuario:
    print(f'{chave}: {usuario.get(chave)}')


