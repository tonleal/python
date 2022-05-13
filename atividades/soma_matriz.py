def soma_matrizes(m1,m2):


    n1_linha = len(m1)
    n2_linha = len(m2)

    n1_coluna = len(m1[0])
    n2_coluna = len(m2[0])

    if n1_linha != n2_linha or n1_coluna != n2_coluna:
        return False

    ncolunas= len(m1[0])
    nlinhas = len(m1)
           
    i = 0
    j = 0
    lista3 = []
      
    for i in range(len(m1)):
        linha = []
        for j in range(len(m1[0])):
                soma = m1[i][j] + m2[i][j]
                linha.append(soma)
        lista3.append(linha)
    print(lista3)
    return(lista3)




  
    

    
