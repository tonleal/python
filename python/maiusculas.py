def maiusculas(frase):
    pos = 0
    frase = frase.replace(" ","")
    i = 0
    j = 0
    string = ""
    
    while i <= len(frase)-1:
        if ord(frase[j]) in range(65,90):
            string += frase[j]
        j = j + 1
        i = i + 1

    return(string)      
            
   
    
   
        
        
