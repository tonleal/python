def menor_nome(nomes):


    c = "b"
    i = 0
    t = 0
    k = 0
    novalista = []
    listat = []
 
    for i in range(len(nomes)):      #coloca todos os nomes sem espaço
        nomestring = nomes[i].strip()
        novalista.append(nomestring)
       
    for t in range(len(novalista)): #cria uma lista com o tamanho de cada nome
        texto = novalista[t]
        tamanho = int(len(texto))
        listat.append(tamanho)

    min_t = min(listat)
    lista_minimos = []

    for k in range(len(listat)):
        if len(novalista[k])==min_t:
            lista_minimos.append(novalista[k].capitalize())

    return(str(lista_minimos))
    
            
           
        
                     
 

    
