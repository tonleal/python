def lista():


    a = [] # lista inicial
    c = "b"
    i = 0
    t = 0
    k = 0
    novalista = []
    listat = []

    while c != "n":
        b = input('digite um nome: ')
        a.append(b)
        c = input('mais algum? [s] ou [n]')   

    print(a)

    for i in range(len(a)):      #coloca todos os nomes sem espaço
        nomestring = a[i].strip()
        novalista.append(nomestring)
       
    print(novalista)

    for t in range(len(novalista)): #cria uma lista com o tamanho de cada nome
        texto = novalista[t]
        tamanho = int(len(texto))
        listat.append(tamanho)

    min_t = min(listat)
    lista_minimos = []

    for k in range(len(listat)):
        if len(novalista[k])==min_t:
            lista_minimos.append(novalista[k].capitalize())

    print(lista_minimos)
            
           
        
                     
 

    
