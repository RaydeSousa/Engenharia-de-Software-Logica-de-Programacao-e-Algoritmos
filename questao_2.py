# Mensagem de boas vindas e cardápio da loja
print("Bem-vindo a Loja de Gelados do Ray de Sousa")

print("------------------ CARDÁPIO ------------------")
print("----------------------------------------------")
print("--- | Tamanho | Cupuaçu (CP) | Açaí (AC) | ---")
print("--- |    P    |    R$ 9.00   |  R$ 11.00 | ---")
print("--- |    M    |   R$ 14.00   |  R$ 16.00 | ---")
print("--- |    G    |   R$ 18.00   |  R$ 20.00 | ---")
print("----------------------------------------------")

# Variável para acumular os valores dos pedidos, caso faça mais de um
valor_total = 0

# Loop para manter o programa funcionando enquanto houver mais pedidos
continuar = True
while continuar:
    
    # Variável para armazenar o sabor desejado
    sabor_desejado = input("Digite o sabor desejado (CP/AC): ").upper()
    # Verificar se o sabor digitado é válido
    if sabor_desejado not in ("CP", "AC"):
        print("Sabor inválido, tente novamente.")
        # Print vazio para quebrar linha
        print()
        # Se o sabor for inválido, o "continue" irá reiniciar o loop
        continue
    
    # Variável para armazenar o tamanho desejado
    tamanho_desejado = input("Digite o tamanho desejado (P/M/G): ").upper()
    # Verificar se o tamanho digitado é válido
    if tamanho_desejado not in ("P", "M", "G"):
        print("Tamanho inválido, tente novamente.")
        # Print vazio para quebrar linha
        print()
        # Se o sabor for inválido, o "continue" irá reiniciar o loop
        continue
    
    # Condicional para precificar os valores dos pedidos

    # Precificação do sabor "Cupuaçu" com os tamanhos P, M e G
    if sabor_desejado == "CP":
        if tamanho_desejado == "P":
            valor = 9
        elif tamanho_desejado == "M":
            valor = 14
        # Se o tamanho desejado for G, caíra no else
        else:
            valor = 18
        # Variável para a gente usar no print mostrando o sabor escolhido, tamanho e preço    
        sabor = "Cupuaçu"
    
    # Precificação do sabor "Açaí" com os tamanhos P, M e G
    if sabor_desejado == "AC":
        if tamanho_desejado == "P":
            valor = 11
        elif tamanho_desejado == "M":
            valor = 16
        # Se o tamanho desejado for G, caíra no else
        else:
            valor = 20
        # Variável para a gente usar na mensagem mostrando o sabor escolhido, tamanho e preço    
        sabor = "Açaí"
    
    # Mensagem mostrando o sabor e tamanho escolhidos e o preço
    print(f"Você pediu um {sabor} tamanho {tamanho_desejado}: R${valor:.2f}")
    # Print vazio para quebrar linha
    print()

    # Valor do pedido sendo adicionado no valor total, assim é possível fazer mais de um e acumular
    valor_total += valor
    
    # Mensagem perguntando se deseja adicionar mais alguma coisa
    adicionar_algo = input("Deseja mais alguma coisa? (S/N): ").upper()
    # Print vazio para quebrar linha
    print()
    # Se sim, o "continue" faz o loop voltar ao início
    if adicionar_algo == "S":
        continue
    # Se não, a variável "continuar" recebe o valor "False", encerrando o loop
    else:
        continuar = False
    
    # Mensagem final mostrando o valor total a ser pago
    print(f"O valor total a ser pago: R${valor_total:.2f}")
    # Eu achei legal adicionar uma mensagem de agradecimento
    print("Obrigado pela compra e volte sempre!")