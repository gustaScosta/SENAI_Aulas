try:
    n1  = int(input('>>>'))
    n2  =  int(input('>>'))
    soma  =  n1 + n2
    lista  =  [n1, n2]
    i =  int(input('Indice: '))
    print(lista[i])
    numero =  int(input('numero:  '))
    print(float(numero))
    print(n1/n2)
    
except TypeError as erro:
    # tentando fazer o calculo aritmético
    # entre um numero e uma letra...
    print(erro)
except ValueError as erro:
    # quando tento imprimir uma letra em um input de numero
    print(erro)
except IndexError as erro:
    # indice que não existe na lista
    print(erro)
except ZeroDivisionError as erro:
    print(erro)
else:
    print('Erro não identificado')
finally:
    print('fim carregamento...')