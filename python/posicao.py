def busca(lista, elemento):

    posicao = 0 
    while posicao <= (len(lista) - 1):
        for i in lista:
            if i == elemento:
                return posicao
            else:
                posicao = posicao + 1
        return False


