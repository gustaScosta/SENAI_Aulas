lista = []
#              ...-5-4-3-2-1         
lista_2 = [1,2,3,4,5,6,7,8,9]
#          0 1 2 3 4 5 6 7 8

print(lista_2[8])


#Funções para adcionar em uma lista

lista_2.append(110) #adciona apenas um dado

print(lista_2)

lista_2.insert(300) #adciona na posição citada

lista_2.extended(10,20,30,40) #adciona varios de uma vez
print(lista_2) 

lista_2 += (201,202,203) #
print(lista_2)

#remover dados

lista_2.remove() #remove o que você selecionar
print(lista_2)

lista_2.pop() #Remove o último valor
print(lista_2)

lista_2.pop(0) #Remove de onde você selecionou
print(lista_2)

del lista_2[6] #Remove da posição selecionada
print(lista_2)

#Fatiamento - slice
novalista = lista_2[:] #Apaga de uma ponta a outra

novalista = lista_2[5:9] #Apaga entre um numero e o outro    START:STOP