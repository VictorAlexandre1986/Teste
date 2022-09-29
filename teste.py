variavel = 'valor'

def func():
    print(variavel)


def func2(arg=None):
    arg=arg.replace('v','c')
    return arg

func()
outra_variavel=func2(variavel)
print(outra_variavel)

l3 = list(range(100))

ex=[i for i in l3 if i % 3 == 0]
print(ex)

ex2 = [v if v % 2 == 0 and v % 3 == 0 else 0 for v in l3]
print(ex2)

d1 = {f'chave_{x}': x**2 for x in range(5)}
print(d1)

nome='Victor Alexandre'

gerador = (letra for letra in nome)

for x in gerador :
    print(x)


dicionario = {x:x**2 for x in range(10)}
print(dicionario)

lista_soma=[]
lista = [1,2,3,4,5,6]
lista2 = [1,2,3,4]
for i in range(len(lista2)):
    lista_soma.append(lista[i] + lista2[i])
print(lista_soma)

lista_soma2 = [x+y for x,y in zip(lista,lista2)]
print(lista_soma2)

def multiplica(lista):
    acum=1
    for i in lista:
        acum *= i
    return acum

valor = multiplica(lista)
print(valor)