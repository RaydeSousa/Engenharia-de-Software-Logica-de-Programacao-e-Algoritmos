# Mensagem de boas vindas.
print("Bem-vindo a Loja do Ray de Sousa!")

# Variável para armazenar o valor do produto
valor_produto = float(input("Entre com o valor do produto: "))

# Variável para armazenar a quantidade do produto
quantidade_produto = float(input("Entre com a quantidade do produto: "))

# Multiplicação do valor * quantidade para obter o valor total
valor_total = valor_produto * quantidade_produto

# Se o valor total for menor que 2500, não terá desconto
if valor_total < 2500:
   print(f"Valor SEM desconto: R${valor_total:.2f}")
   print(f"Valor COM desconto: R${valor_total:.2f}")

# Se o valor total for maior ou igual a 2500 e menor que 6000, o desconto será de 4%
elif valor_total >= 2500 and valor_total < 6000:
   
   desconto = valor_total - (valor_total * 4 / 100)
   print(f"Valor SEM desconto: R${valor_total:.2f}")
   print(f"Valor COM desconto: R${desconto:.2f}")

# Se o valor total for maior ou igual a 6000 e menor que 10000, o desconto será de 7%
elif valor_total >= 6000 and valor_total < 10000:
   
   desconto = valor_total - (valor_total * 7 / 100)
   print(f"Valor SEM desconto: R${valor_total:.2f}")
   print(f"Valor COM desconto: R${desconto:.2f}")

# Se o valor total for maior ou igual a 10000, o desconto será de 11%.
else: 
   desconto = valor_total - (valor_total * 11 / 100)
   print(f"Valor SEM desconto R${valor_total:.2f}")
   print(f"Valor COM desconto R${desconto:.2f}")