
# Prova - Adega

# Declaração de Variáveis
compra = float(0)
loop = 0

# Entrada do Nome
print("[ Adega Dois Irmãos ]")
usuario = input("Digite o seu nome: ")
print(f"Seja Bem Vindo {usuario} à Adega Dois Irmaõs!")

# Entrada dos Dados
while loop == 0:
    print("\n-- Sua compra está no valor de: R$ %.2f --" % compra)

    # Lista dos Produtos
    print("\n[ Lista de Compras ]")
    print("0 - Encerrar a Compra!")
    print("1 - Heineken 269ml: R$ 6,52")
    print("2 - Skol 350ml: R$ 4,99")
    print("3 - Coca-Cola 350ml: R$ 5,56")
    print("4 - Carteira de Derby: R$ 16,40")
    print("5 - Derby solto 1un: R$ 01,50")
    escolha = int(input("O que deseja comprar: "))

    # Validação dos Produtos
    if escolha == 1:
        quantidade = int(input("Quantas Heineken deseja: "))
        compra += 6.52 * quantidade

    elif escolha == 2:
        quantidade = int(input("Quantas Skol deseja: "))
        compra += 4.99 * quantidade

    elif escolha == 3:
        quantidade = int(input("Quantas Coca-Cola deseja: "))
        compra += 5.56 * quantidade

    elif escolha == 4:
        quantidade = int(input("Quantas Carteira de Derby deseja: "))
        compra += 16.40 * quantidade

    elif escolha == 5:
        quantidade = int(input("Quntos Derby solto deseja: "))
        compra += 1.50 * quantidade

    elif escolha == 0:
        loop = 1

    else:
        print("! Produto não existe !")

# Encerramento da Compra
else:
    print("\n[ Compra Finalizada! ]")
    print("Total do Valor da Compra: R$ %.2f" % compra)
