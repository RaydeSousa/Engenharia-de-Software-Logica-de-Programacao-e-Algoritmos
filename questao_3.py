# Mensagem de boas vindas
print("Bem vindo a Copiadora do Ray de Sousa")

# Função para escolher o tipo de serviço
def escolha_servico():
    # Loop para manter o programa funcionando até o usuário digitar uma opção válida
    while True:
        print("Digite o serviço desejado: ")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Fotocópia")
        # Variável para armazenar o tipo de serviço escolhido pelo usuário
        servico = input().upper()

        # Condicional para precificar os tipos de serviços conforme a escolha
        if servico == "DIG":
            return 1.10 # Preço por página de digitalização
        elif servico == "ICO":
            return 1.00 # Preço por página de impressão colorida
        elif servico == "IPB":
            return 0.40 # Preço por página de impressão preto e branco
        elif servico == "FOT":
            return 0.20 # Preço por página de fotocópia
        else:
            # Caso o usuário digite uma opção inválida, o loop recomeça
            print("Escolha inválida, digite o tipo de serviço novamente")
            # Print vazio para quebrar linha
            print()
            continue

# Função para escolher o número de páginas
def num_pagina():
    # Loop para manter o programa funcionando até o usuário digitar um número válido
    while True:
        try:
            # Solicita o número de páginas e converte para inteiro
            num_paginas = int(input("Digite o número de páginas: "))

            # Verifica se o número de páginas é aceitável
            if num_paginas > 20000:
                print("Não aceitamos tantas páginas de uma vez.")
                print("Por favor, digite o número de páginas novamente.")
                # Print vazio para quebrar linha
                print()
                continue
            
             # Aplica descontos conforme a quantidade de páginas
            if num_paginas < 20:
                desconto = 1.00 # Sem desconto
            elif num_paginas >= 20 and num_paginas < 200:
                desconto = 0.85 # 15% de desconto
            elif num_paginas >= 200 and num_paginas < 2000:
                desconto = 0.80 # 20% de desconto
            elif num_paginas >= 2000 and num_paginas < 20000:
                desconto = 0.75 # 25% de desconto
            else:
                desconto = 1.00 # Caso padrão (não deve ocorrer)

            # Retorna o valor ajustado pelo desconto
            return num_paginas * desconto

        # Caso o usuário digite algo que não seja número, exibe mensagem de erro
        except(ValueError):
            print("Valor não numérico! Tente novamente.")
            # Print vazio para quebrar linha
            print()

# Função para escolher serviços adicionais
def servico_extra():
    # Loop para manter o programa funcionando até o usuário escolher uma opção válida
    while True:
        print("Deseja adicionar algum serviço?")
        print("1 - Encadernação Simples - R$ 15.00")
        print("2 - Encadernação Capa Dura - R$ 40.00")
        print("0 - Não desejo mais nada")
        # Armazena a escolha do serviço adicional
        servico_adicional = int(input())
        
        # Condicionais para retornar o valor do serviço adicional
        if servico_adicional == 1:
            return 15.00
        elif servico_adicional == 2:
            return 40.00
        elif servico_adicional == 0:
            return 0.00
        # Caso o usuário digite uma opção inválida
        else:
            print("Opção inválida, digite 1, 2 ou 0.")
            # Print vazio para quebrar linha
            print()

# Função principal para a execução do programa
def main():
    # Chama as funções e armazena os retornos em variáveis
    servico = escolha_servico()     # Preço do serviço principal
    paginas = num_pagina()          # Quantidade (ajustada pelo desconto)
    extra = servico_extra()         # Valor do serviço adicional

    # Calcula o valor total do pedido
    total = (servico * paginas) + extra

    # Exibe o valor total formatado com duas casas decimais
    print(f"Total: R${total:.2f} (serviço: {servico:.2f} * páginas: {paginas:.0f} + extra: {extra:.2f})")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()