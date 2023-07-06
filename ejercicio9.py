def potencia(a,b):
    if b < 0:
        return "nil"
    else:
        resultado = 1
        for i in range(b):
            resultado = resultado * a
        return resultado
    
