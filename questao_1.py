# Aqui mostro o print de boas vindas.
print("Bem-vindo a Loja do Ray de Sousa!")

# Aqui solicito o valor do produto com um input e salvo na variável valor_produto.
valor_produto = float(input("Entre com o valor do produto: "))

# Aqui solicito a quantidade do produto com um input e armazeno na variável quantidade_produto
quantidade_produto = float(input("Entre com a quantidade do produto: "))

# Aqui é feito a multiplição do valor do produto * quantidade do produto e armazeno na variável valor_total.
valor_total = valor_produto * quantidade_produto

# Agora vamos aplicar os descontos utilizando um if-elif-else com a variável valor_total.

# Nesse primeiro if, se o valor total for menor que 2500, não será aplicado nenhum desconto.
if valor_total < 2500:
   print(f"Valor SEM desconto: R${valor_total:.2f}")
   print(f"Valor COM desconto: R${valor_total:.2f}")

# Nesse elif se o valor total for maior ou igual a 2500 e menor que 6000, o desconto será de 4%.
elif valor_total >= 2500 and valor_total < 6000:
   
   desconto = valor_total - (valor_total * 4 / 100)
   print(f"Valor SEM desconto: R${valor_total:.2f}")
   print(f"Valor COM desconto: R${desconto:.2f}")

# Nesse elif se o valor total for maior ou igual a 6000 e menor que 10000, o desconto será de 7%.
elif valor_total >= 6000 and valor_total < 10000:
   
   desconto = valor_total - (valor_total * 7 / 100)
   print(f"Valor SEM desconto: R${valor_total:.2f}")
   print(f"Valor COM desconto: R${desconto:.2f}")

# Nesse elif se o valor total for maior ou igual a 10000, o desconto será de 11%.
elif valor_total >= 10000:
   desconto = valor_total - (valor_total * 11 / 100)
   print(f"Valor SEM desconto R${valor_total:.2f}")
   print(f"Valor COM desconto R${desconto:.2f}")

else:
  print("Valor inválido")

# OBS: O else no final não tem utilidade nesse caso, pois se digitarmos uma letra no input, vai dar erro.
# Daria para resolver utilizando um try/except, mas não coloquei pois não foi uma exigência da atividade.