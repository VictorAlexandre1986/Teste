from random import choice

senha=''

valores1=[x for x in range(64,90)]
valores2=[x for x in range(97,122)]
valores1.append(35)
valores1.append(36)
valores1.append(37)
valores1.append(38)
valores3= valores1 + valores2
senha=''


def gerar(senha,qtd_char):        
    for valor in range(qtd_char):
        caracter = chr(choice(valores3))
        senha += caracter
    return senha

if __name__=='__main__':
    print(gerar(senha,10))
