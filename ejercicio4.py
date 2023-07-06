def deducir_clave(cadena_de_entrada,clave_de_cifrado):
    abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    list_cadena = list(cadena_de_entrada)
    list_cifrado = list(clave_de_cifrado)
    descifrado = []
    for j in range(len(list_cadena)):
        letras_cadena = list_cadena[j]
        letras_cifrado = list_cifrado[j%len(list_cifrado)]
        a = abecedario.index(letras_cadena)
        b = abecedario.index(letras_cifrado)
        indice_descifrado = (a-b)%len(abecedario)

        descifrado.append(abecedario[indice_descifrado])

    return ''.join(descifrado)

print(deducir_clave("HFNIMVOSNA", "ABCXYZ"))
