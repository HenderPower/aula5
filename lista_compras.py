def mostrar():
    compras = ["Arroz", "Molho de tomate", "Biocarbonado de Sódio", "Doritos", "Oleo"]

    for contador, compras in enumerate(compras, start=1):
        print(f" {contador}. {compras}")
        contador += 1

def cadastrar():
    compras = ["Arroz", "Molho de tomate", "Biocarbonado de Sódio", "Doritos", "Oleo"]

    compras.append("Carne Bovina")
    print(compras)


def excluir():
    compras = ["Arroz", "Molho de tomate", "Biocarbonado de Sódio", "Doritos", "Oleo"]
    compras.remove("Oleo")

    print(compras)


def modificar():
    compras = ["Arroz", "Molho de tomate", "Biocarbonato de Sódio", "Doritos", "Oleo"]
    compras[2] = "Agua"
    compras.index("Biocarbonato de Sódio")


while True:
    print("1- Mostrar Lista")
    print("2- Cadastrar Item na Lista")
    print("3- Excluir Item da Lista")
    print("4- Modificiar item da lista")
    print("0- Sair")


    opcao = input("Escolha uma ação: " )

    if opcao == "1":
        mostrar()

    elif opcao == "2":
        cadastrar()

    elif opcao == "3":
        excluir()

    elif opcao == "4":
        modificar()
    
    elif opcao == "0":
        print("Saindo do programa")
        break

    else:
         print("Opção inválida, por favor seleciona um número da lista.")





