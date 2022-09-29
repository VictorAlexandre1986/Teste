def autorizacao(idade):
    msg = "Autorizado" if idade >= 18 else "Não autorizado"
    print(msg)


autorizacao(36)

lista=[1,2,3,4,5,6]

def multiplica(lista):
    r=1
    for valor in lista:
        r*=valor
    return r



print(multiplica(lista))

from functools  import reduce
total = reduce(lambda ac,i:i*ac,lista)
print(total)

from time import time
from time import sleep

def master(funcao):
    def slave():
        start=time()
        print('Funcao decorada')
        funcao()
        end=time()
        res=(end - start) * 1000
        print (f'A funcao levou {res} segundos')
    return slave


def fala_oi():
    print('oi')

funcao=master(fala_oi)
funcao()