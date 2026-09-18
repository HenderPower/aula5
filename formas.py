def formula_circulo():
    pi = 3.1415
    raio = float(input("Difgite o valor do raio: "))
    area_circulo = pi * raio ** 2
    print(f"A área do círculo é: {area_circulo}")

def formula_triangulo():
    base = float(input("Digite o valor da base: "))
    altura = float (input("Digite o valor da altura: "))
    area_triangulo = (base * altura) /2
    print(f"A área do triângulo é: {area_triangulo}")

def formula_quadrado():
    area_quadrado = float(input("Digite o valor do quadrado: "))
    area_total = area_quadrado ** 2
    print(f"A área do quadrado é: {area_total}")

def formula_cubo():
    area_cubo = float(input("Digite o valor do cubo: "))
    area_totalcubo = area_cubo ** 3
    print(f"A área total do cubo é: {area_totalcubo}")

def formula_retangulo():
    base_retangulo = float(input("Digite a base do retângulo: "))
    altura_retangulo = float(input("Digite a altura do retângulo: "))
    area_retangulo = base_retangulo * altura_retangulo
    print(f"A área total do retângulo é: {area_retangulo}")

def formula_paralelogramo():
    base_paralelgramo = float(input("Digite o valor da base do paralelogramo: "))
    altura_paralelogramo = float(input("Digite o valor da altura do paralelogramo: "))
    area_paralelgramo = base_paralelgramo * altura_paralelogramo
    print(f"A area total do Paralelogramo é: {area_paralelgramo}")

def formula_trapezio():
    base1 = float(input("Digite o valor da primeira base do trapézio: "))
    base2 = float(input("Digite o valor da segunda base do trapézio: "))
    altura_trapezio = float(input("Digite o valor da altura: "))

    if base1 > base2:
            area_trapezio = (base1 * base2) * altura_trapezio / 2
            print(f"A área total do losango é: {area_trapezio}")
    
    elif base1 < base2:
            area_trapezio = (base2 * base1) * altura_trapezio / 2
            print(f"A área do losango é: {area_trapezio}")
    
    else:
            print("O valor das 2 bases não pode ser igual!")

def formula_losango():
    diagonal1 = float(input("Digite o valor da primeira diagonal: "))
    diagonal2 = float(input("Digite o valor da segunda diagonal: "))

    if diagonal1 > diagonal2:
        area_losango = (diagonal1 * diagonal2) / 2
        print(f"A área total do losango é: {area_losango}")

    elif diagonal1 < diagonal2:
        area_losango = (diagonal2 * diagonal1) / 2
        print(f"A área do losango é: {area_losango}")

    else:
        print("O valor das 2 diagonais não pode ser igual pois vai se tornar um quadrado!")



while True:
    print("1 - Círculo")
    print("2- Triângulo")
    print("3- Quadrado")
    print("4- Retangulo")
    print("5- Paralelogramo")
    print("6- Losango")
    print ("7- Trapézio")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        formula_circulo()

    elif opcao == "2":
        formula_triangulo()

    elif opcao == "3":
        formula_quadrado()

    elif opcao == "4":
        formula_retangulo()

    elif opcao == "5":
        formula_paralelogramo()

    elif opcao == "6":
        formula_losango()

    elif opcao == "7":
        formula_trapezio()

    elif opcao == "0":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida, por favor ponha o valor correto!")

