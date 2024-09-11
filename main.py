valor = 26

def cadeia_de_caracteres(valor):
    lista = []
    if valor <= 26:
        for i in range(valor):
            caratere = chr(ord("a") + i)
            lista.append(caratere)
    else:    
        return lista   
    return lista

print(cadeia_de_caracteres(valor))
