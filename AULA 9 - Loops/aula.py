notas = True


dados = {
    'notas':[],
    'total':[],
    }
while notas == True:
    dados['notas'].append(int(input("Adcione uma nota:")))
    continuar = input("Deseja adcionar mais notas? s/n")
    if continuar == 's':
        notas = True
    else:
        notas = False
media_aluno1 = sum(dados['notas'])/len(dados['notas'])
print(media_aluno1)


""" sequencia = []



for i in range(5):
    print(i)

contador = 0
while contador < 5:
    contador  = contador + 1
    print(contador) """

# e -commerce
dados = {
    'login':'@bea',
    'senha':'1234',
    'carrinho':[],
    'total':[],
    'produtos':['', "A","B","C","D"],
    'valores':[0,100.50,250.55,4000.0,1000.0],
    
    }

# print(dados)

for x in range(3):
    senha = input('digite sua senha: ')
    login = input('Digite seu login: ')
    if senha  == dados['senha'] and login == dados['login']:
        print('Seja bem vindo(a)')
        pr =  input('Deseja comprar? s/n')
        while pr == 's':
            print(f'''Produtos:, 
            
            {dados['produtos'][1]} - 1
            {dados['produtos'][2]} - 2
            {dados['produtos'][3]} - 3
            {dados['produtos'][4]} - 4
            
            ''') #Tres aspas para pular linha sem usar \n
            produto = int(input('Escolha o produto'))
            dados['carrinho'].append(dados['produtos'][produto]) # adciona o produto no carrinho
            dados['total'].append(dados['valores'][produto]) #adciona o preço do produto no total
            print(dados['carrinho'])
            print('R$', sum(dados['total']))
            v  =   sum(dados['total'])
            pr =  input('Deseja continuar? s/n')
        else:
            print('Forma de pagamento')
            pag = ['','pix - 1', 'cc - 2', 'cd - 3']
            print(pag)
            print(pag[int(input('Escolha a forma> 1,2,3'))])
            print('-------------------------------------')
            print('R$', v) 
            print('-------------------------------------')  
            print('Obrigada volte sempre')
            break 

        
        
        
    else:
        print('tente novamente...')
else:
    print('Senha bloqueada')



n =  int(input('numero: '))


for x in range(1,11):
    c = x * n
    print(n , 'x', x , '=', c ) 