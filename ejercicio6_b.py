def ordenar(n):
    list_a = n.splitlines()
    list_b = []
    orden = {
        "El día 12 de Navidad mi verdadero amor me dio":0,
        "12 bateristas tocando el tambor,":1,
        "tubería de 11 gaiteros,":2,
        "10 señores un salto,":3,
        "9 damas bailando,":4,
        "8 criadas un ordeño,":5,
        "7 cisnes nadando,":6,
        "6 gansos una puesta,":7,
        "5 anillos de oro,":8,
        "4 pájaros cantando,":9,
        "3 gallinas francesas,":10,
        "2 tórtolas y":11,
        "1 perdiz en un peral.":12
    }
    list_b = sorted(list_a, key= lambda x: orden[x])

    return "\n".join(list_b)
