import random

# -------------------------------------------
# FUNÇÃO: GERAR CARTELA
# -------------------------------------------
def gerar_cartela(sigla):
    cartela = [[0 for _ in range(5)] for _ in range(5)]
    faixas = [(1, 15), (16, 30), (31, 45), (46, 60), (61, 75)]

    for col in range(5):
        numeros = []
        while len(numeros) < 5:
            num = random.randint(faixas[col][0], faixas[col][1])
            if num not in numeros:
                numeros.append(num)
        for lin in range(5):
            cartela[lin][col] = numeros[lin]

    cartela[2][2] = sigla
    return cartela


# -------------------------------------------
# FUNÇÃO: IMPRIMIR CARTELA
# -------------------------------------------
def imprimir_cartela(cartela):
    for linha in cartela:
        for valor in linha:
            if isinstance(valor, int):
                print(f"[{valor:02d}]", end=" ")
            else:
                print(f"[{valor}]", end=" ")
        print()
    print()


# -------------------------------------------
# FUNÇÃO: SORTEAR VALOR
# -------------------------------------------
def sorteia_valor(sorteados):
    if len(sorteados) >= 75:
        return -1
    while True:
        num = random.randint(1, 75)
        if num not in sorteados:
            return num


# -------------------------------------------
# FUNÇÃO: VERIFICAR GANHADOR (CARTELA CHEIA)
# -------------------------------------------
def verifica_ganhador_cheia(cartelas, sorteados):
    for cartela in cartelas:
        venceu = True
        for linha in cartela:
            for valor in linha:
                if isinstance(valor, int) and valor not in sorteados:
                    venceu = False
                    break
            if not venceu:
                break
        if venceu:
            return cartela
    return None


# -------------------------------------------
# FUNÇÃO: VERIFICAR GANHADOR (LINHA, COLUNA, DIAGONAL)
# -------------------------------------------
def verifica_ganhador_LCD(cartelas, sorteados):
    for cartela in cartelas:
        # Linhas
        for linha in cartela:
            if all((not isinstance(v, int)) or (v in sorteados) for v in linha):
                return cartela

        # Colunas
        for c in range(5):
            if all((not isinstance(cartela[l][c], int)) or (cartela[l][c] in sorteados) for l in range(5)):
                return cartela

        # Diagonal principal
        if all((not isinstance(cartela[i][i], int)) or (cartela[i][i] in sorteados) for i in range(5)):
            return cartela

        # Diagonal secundária
        if all((not isinstance(cartela[i][4 - i], int)) or (cartela[i][4 - i] in sorteados) for i in range(5)):
            return cartela

    return None


# -------------------------------------------
# MENU PRINCIPAL
# -------------------------------------------
def main():
    cartelas = []
    sorteados = []
    regra = 1
    sigla = input("Digite suas iniciais (2 letras): ").upper()

    while True:
        print("Escolha a opção:")
        print("1 - Gerar Cartelas")
        print("2 - Definir Regras")
        print("3 - Começar Bingo!")
        print("4 - Encerrar Programa")
        opcao = input(">> ")

        # GERAR CARTELAS
        if opcao == "1":
            cartelas = []
            qtd = int(input("Informe a quantidade de Cartelas a serem Geradas: "))
            for _ in range(qtd):
                cartelas.append(gerar_cartela(sigla))
            print()

        # DEFINIR REGRAS
        elif opcao == "2":
            print("Escolha a regra:")
            print("1 - Linha, Coluna, Diagonal (padrão)")
            print("2 - Cartela Cheia")
            r = input(">> ")
            if r == "2":
                regra = 2
            else:
                regra = 1
            print()

        # COMEÇAR BINGO
        elif opcao == "3":
            if not cartelas:
                print("Nenhuma cartela gerada!\n")
                continue

            sorteados = []
            print("Começando o Bingo!")
            print()

            while True:
                num = sorteia_valor(sorteados)
                if num == -1:
                    print("Todos os números já foram sorteados!\n")
                    break
                sorteados.append(num)

                if regra == 2:
                    ganhador = verifica_ganhador_cheia(cartelas, sorteados)
                else:
                    ganhador = verifica_ganhador_LCD(cartelas, sorteados)

                if ganhador:
                    print("Temos um ganhador!!")
                    print()
                    print(f"Sorteados: {len(sorteados)} números")
                    print()

                    # Exibe números sorteados formatados (5 por linha)
                    for i in range(0, len(sorteados), 5):
                        linha = sorteados[i:i + 5]
                        for v in linha:
                            print(f"[{v:02d}]", end=" ")
                        print()
                    print()

                    # Cartela vencedora
                    imprimir_cartela(ganhador)
                    break

        # ENCERRAR PROGRAMA
        elif opcao == "4":
            break

        else:
            print("Opção inválida!\n")


# -------------------------------------------
# EXECUÇÃO
# -------------------------------------------
if __name__ == "__main__":
    main()
