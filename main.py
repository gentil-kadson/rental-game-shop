from locador import Locador
from locatario import Locatario
from endereco import Endereco
from item import Item

locadores: list[Locador] = []
locatarios: list[Locatario] = []
itens: list[Item] = []
criar_outra_conta: bool = True
usuario_logado: Locador | Locatario = None
logado: bool = False

def criar_conta():
    while True:   
        print("Que tipo de conta quer criar?")
        print("[1] Locador \n[2] Locatário")
        tipo_conta_a_criar = input()
        
        print("Dados de usuário:")
        cpf_cnpj = input("CPF/CNPJ: ")
        email = input("E-mail: ")
        nome = input("Nome: ")
        senha = input("Senha: ")

        print("Cadastre um endereço:")
        logradouro = input("Digite seu logradouro (Rua, Avenida), número e bairro: ")
        cidade = input("Digite o nome de sua cidade: ")
        estado = input("Digite a sigla de seu estado: ")
        pais = input("Digite o nome do seu país: ")
        endereco = Endereco(logradouro, cidade, estado, pais)  

        if tipo_conta_a_criar == '1':
            print("Quer usar transportadora (você pode mudar depois)?")
            print("[1] Sim \n[2] Não")
            usa_transportadora = input()
            if usa_transportadora == '1':
                locador = Locador(True, endereco, endereco, nome, cpf_cnpj, 1, email, senha, endereco)
                locadores.append(locador)
            else:
                locador = Locador(False, endereco, endereco, nome, cpf_cnpj, 1, email, senha, endereco)
                locadores.append(locador)
        elif tipo_conta_a_criar == '2':
            locatario = Locatario(nome, 2, cpf_cnpj, email, senha, endereco)
            locatarios.append(locatario)
        
        print("Deseja criar outra conta?")
        print("[1] Sim \n[2] Não")
        opcao = input()
        if opcao == '2':
            break

def logar():
    print("Que tipo de usuário é você?")
    print("[1] Locador \n[2] Locatário \n[3] Sair")
    opcao = input()
    print('Essa é a opção: ' + opcao)
    if opcao == '3':
        print("Obrigado por utilizar nossa loja!")
    else:
        email_check = input("Digite o e-mail: ")
        senha_check = input("Digite a senha: ")
        if opcao == '1':
            for locador in locadores:
                if locador.get_email() == email_check and locador.get_senha() == senha_check:
                    return locador
                else:
                    return False
            
        if opcao == '2':
            for locatario in locatarios:
                if locatario.get_email() == email_check and locatario.get_senha() == senha_check:
                    return locatario
                else:
                    return False

def remover_item(id: int) -> bool:
    for item in itens:
        if id == item.get_ident():
            try:
                itens.remove(item)
                return True
            except ValueError:
                return False

while logado == False:
    print("Bem-vindo ao Rental Game Shop!")
    print("Já tem conta?")
    print("[1] Sim \n[2] Não \n[3] Sair")
    ja_tem_conta = input()
    if ja_tem_conta == '1':
        while usuario_logado == None:
            usuario_logado = logar()
        break
    elif ja_tem_conta == '2':
        criar_conta()
    elif ja_tem_conta == '3':
        break

if usuario_logado is not False:
    print(f'Bem vindo, usuário {usuario_logado.get_nome()}.')
    if usuario_logado.get_tipo() == 1:
        pass
    elif usuario_logado.get_tipo() == 2:
        print("O que deseja fazer?")
        print("[1] Cadastrar item \n[2] Excluir item \n[3] Enviar itens")
        opcao = input()

        if opcao == '1':
            nome = input('Nome do item: ')
            preco = input('preco: ')
            item_novo = Item(1, nome, float(preco), True, usuario_logado)
            itens.append(item_novo)
            print('Item cadastrado com sucesso!')
        elif opcao == '2':
            print('Esses são os itens que você tem: ')
            for item in itens:
                if item.get_dono() == usuario_logado:
                    print(item)
            id = input('Digite o id do item que deseja excluir: ')

            if remover_item(id) == True:
                print('Item removido com sucesso!')
            else:
                print('Esse item não está cadastrado.')
        elif opcao == '3':
            print("Esses são os itens que você tem e que foram requisitados:")
            for item in itens:
                if item.get_disponivel() == False:
                    print(item)
            print("Quer enviar-los?")
            print("[1] Sim \n[2] Não")
            enviar = input()
            if enviar == '1':
                usuario_logado.enviar_itens()




# opcao_cadastrar_item = input("Deseja cadastrar um item? [1] Sim \n [2] Não")
# while opcao_cadastrar_item == 1:
#     print("Cadastre seu item: ")
#     ident = input("Código de identificação: ")
#     nome = input("Nome: ")
#     preco = ("Valor: ") 
#     disponivel = input("O item estará disponível para locação? [1] Sim [2] Não")
#     if disponivel == "1": 
#         item = Item(ident, nome, preco, True, locatario)
#     else:
#         item = Item(ident, nome, preco, False, locatario)
#     opcao_cadastrar_item = input("Deseja cadastrar um novo item? [1] Sim [2] Não")

    