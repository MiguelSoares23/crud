frutaria = []

frutaria.append({
    "codigo": "0001",
    "fruta": "maçã",
    "valorKg": 6.90,
    "qtd": 90
})

frutaria.append({
    "codigo": "0002",
    "fruta": "banana",
    "valorKg": 8.90,
    "qtd": 90
})

frutaria.append({
    "codigo": "0003",
    "fruta": "melão",
    "valorKg": 11.00,
    "qtd": 90
})

def inserirFrutas():
    codigo = input("Digite o código da fruta: ")
    fruta = input("Digite o nome da fruta: ")
    valorKg = float(input("Digite o valor por Kg: "))
    qtd = float(input("Digite a quantidade em Kg: "))
    
    nova_fruta = {
        "codigo": codigo,
        "fruta": fruta,
        "valorKg": valorKg,
        "qtd": qtd
    }
    
    frutaria.append(nova_fruta)
    print(f"✅ Fruta '{fruta}' cadastrada com sucesso!\n")


def vendaFrutas():
    nome_fruta = input("Digite o nome da fruta que deseja comprar: ")
    qtd_kg = float(input("Digite a quantidade em Kg: "))
    
    for fruta in frutaria:
        if fruta["fruta"].lower() == nome_fruta.lower():
            if fruta["qtd"] >= qtd_kg:
                total = qtd_kg * fruta["valorKg"]
                fruta["qtd"] -= qtd_kg
                print(f"\n Você comprou {qtd_kg} Kg de {fruta['fruta']}. Total: R$ {total:.2f}")
                print(f"Estoque atualizado: {fruta['qtd']} Kg restantes.\n")
                return
            else:
                print("\nQuantidade solicitada não disponível no estoque.\n")
                return
    print("\n Fruta não encontrada.\n")


def consultarEstoque():
    print("\nEstoque Atual:")
    print("-" * 40)
    for fruta in frutaria:
        print(f"Código: {fruta['codigo']} | Fruta: {fruta['fruta']} | Preço: R$ {fruta['valorKg']:.2f} | Quantidade: {fruta['qtd']} Kg")
    print("-" * 40 + "\n")


def menu():
    while True:
        print("=== Frutaria do Zé ===")
        print("1 - Comprar fruta")
        print("2 - Cadastrar nova fruta")
        print("3 - Consultar estoque")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            vendaFrutas()
        elif opcao == "2":
            inserirFrutas()
        elif opcao == "3":
            consultarEstoque()
        elif opcao == "4":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()
