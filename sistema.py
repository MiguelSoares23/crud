#teste

frutaria = []
maca = {
    "codigo": "0001",
    "fruta": "maçã",
    "valorKg": 6.90,
    "qtd": 90
}

banana = {
    "codigo": "0002",
    "fruta": "banana",
    "valorKg": 8.90,
    "qtd": 90  
}

melao = {
    "codigo": "0003",
    "fruta": "melão",
    "valorKg": 11.0,
    "qtd": 90
}

frutaria.append(maca)
frutaria.append(banana)
frutaria.append(melao)

def inserirFrutas(codigo, fruta, valorKg, qtd):
    frutas = {
        "codigo": codigo,
        "fruta": fruta,
        "valorKg": valorKg,
        "qtd": qtd
    }
    frutaria.append(frutas)

def vendaFrutas(fruta, qtd):
    for i in frutaria:
        if fruta == frutaria[]
        