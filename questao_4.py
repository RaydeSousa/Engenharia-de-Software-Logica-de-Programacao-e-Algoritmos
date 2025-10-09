# Mensagem de boas-vindas
print("Bem vindo a Livraria do Ray de Sousa")

# Lista para armazenar os livros cadastrados
lista_livros = []

# ID global inicial com meu RU para os livros
id_global = 4770284

# Função para cadastrar um novo livro
def cadastrar_livro(id):
    global id_global  # Permite alterar a variável global id_global
    
    print("------------------------------------------")
    print("---------- MENU CADASTRAR LIVRO ----------")
    print(f"Id do livro: {id_global}")  # Exibe o ID que será atribuído
    nome = input("Digite o nome do livro: ")  # Solicita o nome do livro
    autor = input("Digite o autor do livro: ")  # Solicita o nome do autor
    editora = input("Digite a editora do livro: ")  # Solicita a editora

    # Cria um dicionário representando o livro
    livro = {
        'id': id,
        'nome': nome,
        'autor': autor,
        'editora': editora
    }

    # Adiciona o livro à lista de livros
    lista_livros.append(livro.copy())
    print("Livro cadastrado com sucesso!")

# Função para consultar livros
def consultar_livro():
    while True:
        print("------------------------------------------")
        print("---------- MENU CONSULTAR LIVRO ----------")
        print("Escolha a opção desejada: ")
        print("1. Consultar Todos")
        print("2. Consultar por ID")
        print("3. Consultar por Autor")
        print("4. Retornar ao Menu")

        opcao = int(input())

        # Opção 1: Consultar todos os livros cadastrados
        if opcao == 1:
            if not lista_livros:  # Verifica se a lista está vazia
                print("Nenhum livro cadastrado.")
            for livro in lista_livros:
                print(f"id: {livro['id']}")
                print(f"nome: {livro['nome']}")
                print(f"autor: {livro['autor']}")
                print(f"editora: {livro['editora']}")
                print()
        # Opção 2: Consultar livro por ID
        elif opcao == 2:
            id_livro = int(input("Digite o ID do livro: "))
            for livro in lista_livros:
                if id_livro == livro['id']:
                    print(f"id: {livro['id']}")
                    print(f"nome: {livro['nome']}")
                    print(f"autor: {livro['autor']}")
                    print(f"editora: {livro['editora']}")
                    print()
        # Opção 3: Consultar livro por autor
        elif opcao == 3:
            autor_livro = input("Digite o autor do livro: ")
            for livro in lista_livros:
                if autor_livro == livro['autor']:
                    print(f"id: {livro['id']}")
                    print(f"nome: {livro['nome']}")
                    print(f"autor: {livro['autor']}")
                    print(f"editora: {livro['editora']}")
                    print()
        # Opção 4: Retornar ao menu principal
        elif opcao == 4:
            break
        else:
            # Caso o usuário digite uma opção inválida
            print("Opção inválida")
            continue

# Função para remover um livro pelo ID
def remover_livro():
        print("----------------------------------------")
        print("---------- MENU REMOVER LIVRO ----------")
        livro_removido = int(input("Digite o ID do livro a ser removido: "))
        achou = False  # Flag para verificar se o livro foi encontrado

        # Percorre a lista de livros procurando o ID
        for livro in lista_livros:
            if livro_removido == livro["id"]:
                lista_livros.remove(livro)  # Remove o livro encontrado
                print("Livro removido com sucesso!")
                achou = True
                break

        # Caso o livro não seja encontrado
        if not achou:
            print("ID inválido.")

# Loop principal do programa
while True:
    print("------------------------------------")
    print("---------- MENU PRINCIPAL ----------")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Remover Livro")
    print("4. Encerrar Programa")

    opc = int(input(""))

    # Chama a função de cadastrar livro e incrementa o ID global
    if opc == 1:
        cadastrar_livro(id_global)
        id_global += 1
    # Chama a função de consulta de livros
    elif opc == 2:
        consultar_livro()
    # Chama a função de remoção de livros
    elif opc == 3:
        remover_livro()
    # Encerra o programa
    elif opc == 4:
        print("Programa encerrado!")
        break
    else:
        # Caso o usuário digite uma opção inválida
        print("Opção inválida")
        continue
