nome="               victor alexandre               "
print('Retorna a primeira letra maiuscula ',nome.capitalize())

print('Centraliza e completa com espaços em branco',nome.center(20))

print('Conta qts vezes aparace na string a substring ou caracter desejado',nome.count("a"))

msg = 'O rato roeu a roupa do rei de roma'

print('Verifica se termina com ',msg.endswith('roma'))

print('Verefica se esta presente a string e retorna o indice ',msg.find('roeu'))

print('Retorna o indice da string ',msg.index('rei'))

print('Verifica se possui caracterers alfabetico ',msg.isalpha())

print('Converte para maiusculo',msg.upper())

print('Substitui',msg.replace('o','0'))

print('Converte para minusculo',msg.lower())

print('Remove espaços em brancos a direita',nome.rstrip())

print('Remove espaços em brancos a esquerda',nome.lstrip())

print('Remove espaços em brancos a direita e esquerda',nome.strip())

print('Verifica se começa ',msg.startswith('O'))

print('Divide a string e devolve em uma lista ',msg.split())

lista = msg.split()
#Unindo os dados de uma lista em uma string
unindo = ' '.join(lista)

print('Verifica se a string é alfanumerico',msg.isalnum())

print('Verifica se a string está toda em minusculo ',msg.islower())

print('Verifica se é caracteres da tabela ASCII', msg.isdigit())

print('Verifica se a string começa com maiúscula', msg.istitle())

print('Verifica se a string está em toda maiuscula',msg.isupper())

print('Retorna uma tupla seperado pela string informada',msg.partition("roeu"))
