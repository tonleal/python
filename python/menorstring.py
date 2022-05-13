lista = ['Ana', 'eu', 'VOCÊ']
print(lista[0])
tamanholista = len(lista)
print(tamanholista)

def menorstring(lista):
    novalista = []
    i = 0
    while i < tamanholista:
        menor = lista[i].lower()
        novalista.append(menor)
        i = i + 1

    listadeord = []
    i = 0
    while i < tamanholista:
        nome = novalista[i]
        caracter = nome[0]
        numero = ord(caracter)
        listadeord.append(numero)
        i = i + 1

    print(listadeord)
        
    
