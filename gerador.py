import time

def gera():
    for n in range(100):
        yield(n)
        time.sleep(0.5)

g = gera()

#for n in g:
#    print(n)


(l for l in range(100))


produtos = [
    {'nome':'camiseta','preco':10},
    {'nome':'bermuda','preco':20}
]

novos = map(lambda p:p['preco']*2,produtos)
for i in novos:
    print(i)


def aumenta(p):
    p['preco']=p['preco']*2
    return p

novos2 = map(aumenta,produtos)
for i in novos2:
    print(i)