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
                locador = Locador(nome, cpf_cnpj, 1, email, senha, endereco, [])
                locadores.append(locador)
            else:
                locador = Locador(nome, cpf_cnpj, 1, email, senha, endereco, [])
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

def processo_alugamento():
    while True:
        print("Esses são os itens disponíveis para alugar:")
        for item in itens:
            if item.get_disponivel() == True:
                print(item)

        id_item = input("Digite o ID do item que deseja alugar: ")
        for item in itens:
            if item.get_ident() == int(id_item) and item.get_disponivel() == True:
                item.set_disponivel(False)
                usuario_logado.adicionar_item(item)

        print("Deseja alguar mais algum?")
        print("[1] Sim \n[2] Não")
        alugar_mais = input()
        if alugar_mais == '2':
            break

def processo_devolver_item():
    while True:
        id_item_a_devolver = input("Digite o id do item que quer devolver: ")
        
        for item in usuario_logado.get_itens_escolhidos():
            if item.get_ident() == int(id_item_a_devolver) and item.get_entregue() == True:
                item.set_entregue(False)
                item.set_alugado(False)
                item.set_disponivel(True)
                usuario_logado.get_itens_escolhidos().remove(item)

        for item in itens:
            if item.get_ident() == int(id_item_a_devolver) and item.get_entregue() == True:
                item.set_entregue(False)
                item.set_alugado(False)
                item.set_disponivel(True)

        print("Item devolvido com sucesso!")
        print("Deseja devolver outro?")
        print("[1] Sim \n[2] Não")
        devolver_outro = input()
        if devolver_outro == '2':
            break

def processo_confirmar_alugamento():
    while True:
        id_do_item_confirmado = input("Digite o id do item confirmado: ")
        confirmou = False
        for item in usuario_logado.get_itens_escolhidos():
            if item.get_ident() == int(id_do_item_confirmado) and item.get_alugado() == False:
                item.set_alugado(True)
                confirmou = True
                break
        for item in itens:
            if item.get_ident() == int(id_do_item_confirmado) and item.get_alugado() == False:
                item.set_alugado(True)
                print("O item ficou alugado? " + item.get_alugado())
                break
        if confirmou == True:
            print("Item confirmado! Deseja alugar outro?")
            alugar_outro = input("[1] Sim \n[2] Não")
            if alugar_outro == '2':
                break

def processo_cadastrar_item():
    nome = input('Nome do item: ')
    preco = input('preco: ')
    item_novo = Item(nome, float(preco), True, usuario_logado, False, False, False)
    itens.append(item_novo)
    print('Item cadastrado com sucesso!')

while True:
    print("Bem-vindo ao Rental Game Shop!")
    print("Já tem conta?")
    print("[1] Sim \n[2] Não \n[3] Sair")
    ja_tem_conta = input()
    if ja_tem_conta == '1':
        while usuario_logado == None or usuario_logado == False:
            usuario_logado = logar()
    elif ja_tem_conta == '2':
        criar_conta()
    elif ja_tem_conta == '3':
        break

    if usuario_logado is not False and usuario_logado is not None:
        print(f'Bem vindo, usuário {usuario_logado.get_nome()}.')
            
        if usuario_logado.get_tipo() == 1:
            while True:
                print("O que deseja fazer?")
                print("[1] Alugar itens \n[2] Ver lista de itens que já chegaram \n[3] Pagar itens alugados \n[4] Sair")
                o_que_fazer = input()
                
                if o_que_fazer == '1':
                    processo_alugamento()
                elif o_que_fazer == '2':
                    print("Esses são os itens que já chegaram")
                    for item in usuario_logado.get_itens_entregues():
                        print(item)

                    print("Deseja devolver algum item?")
                    print("[1] Sim \n[2] Não")
                    devovler = input()
                    if devovler == '1':
                        processo_devolver_item()
                elif o_que_fazer == '3':
                    print("Esses são os itens pedentes:")
                    for item in usuario_logado.get_itens_escolhidos():
                        print(item)
                    
                    processo_confirmar_alugamento()
                elif o_que_fazer == '4':
                    usuario_logado = None
                    break

        elif usuario_logado.get_tipo() == 2:
            while True:
                print("O que deseja fazer?")
                print("[1] Cadastrar item \n[2] Excluir item \n[3] Enviar itens \n[4] Sair")
                opcao = input()

                if opcao == '1':
                    processo_cadastrar_item()
                elif opcao == '2':
                    print('Esses são os itens que você tem: ')
                    for item in itens:
                        if item.get_dono() == usuario_logado:
                            print(item)
                    id = input('Digite o id do item que deseja excluir: ')

                    if remover_item(int(id)) == True:
                        print('Item removido com sucesso!')
                    else:
                        print('Esse item não está cadastrado.')
                elif opcao == '3':
                    print("Esses são os itens que você tem e que foram requisitados:")
                    tem_item_pra_enviar = False
                    for item in itens:
                        if item.get_disponivel() == False and item.get_alugado() == True and item.get_dono() == usuario_logado and item.get_entregue() == False:
                            print(item)
                            tem_item_pra_enviar = True
                    if tem_item_pra_enviar == False:
                        print('Você não tem nenhum item para enviar.')
                    else:
                        print("Quer enviá-los?")
                        print("[1] Sim \n[2] Não")
                        enviar = input()
                        if enviar == '1':
                            for item in itens:
                                if item.get_disponivel() == False and item.get_alugado() == True and item.get_dono() == usuario_logado:
                                    item.set_entregue(True)
                            for locador in locadores:
                                for item in locador.get_itens_escolhidos():
                                    if item.get_disponivel() == False and item.get_alugado() == True and item.get_dono() == usuario_logado:
                                        item.set_entregue(True)
                elif opcao == '4':
                    usuario_logado = None
                    break

print("Obrigado por utilizar o nosso programa!")                    




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

    