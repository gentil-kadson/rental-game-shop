from locador import Locador
from locatario import Locatario
from endereco import Endereco
from estoque import Estoque

locadores: list[Locador] = []
locatarios: list[Locatario] = []
criar_outra_conta: bool = True
usuario_logado: Locador | Locatario = None
logado: bool = False
estoque = Estoque([])

def criar_conta():
    '''
    Inicia o processo de criação de conta do usuário. Esta função irá criar um locador, caso o usuário digite 1, ou um locatário, caso o usuário digite 2.
    '''
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
    '''
    Loga o usuário no sistema. A função irá retornar um objeto ou do tipo Locador ou do tipo Locatario -- isso depende de qual tipo de usuário o usuário é. Caso o sistema não consiga logar, volta-se para a tela inicial do sistema.
    '''
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
                if locador.logar(email_check, senha_check) == True:
                    return locador
                else:
                    break
            
        if opcao == '2':
            for locatario in locatarios:
                if locatario.logar(email_check, senha_check):
                    return locatario
                else:
                    break

def processo_locacao():
    '''
    Inicia o processo de locação de um item disponível para ser alugado. Nessa função, o usuário levará o item apenas para a seção de pagamentos pendentes; ele não estará confirmando a locação do item. Caso ele aloque algum item, ele será adicionado à lista de itens escolhidos do usuário e será marcado como indisponível. Nesse processo, o usuário poderá alocar quantos itens quiser.
    '''
    while True:
        print("Esses são os itens disponíveis para alugar:")
        for item in estoque.get_lista_itens():
            if item.get_disponivel() == True:
                print(item)

        id_item = input("Digite o ID do item que deseja alugar: ")
        for item in estoque.get_lista_itens():
            if item.get_ident() == int(id_item) and item.get_disponivel() == True:
                item.set_disponivel(False)
                usuario_logado.adicionar_item(item)

        print("Deseja alugar mais algum?")
        print("[1] Sim \n[2] Não")
        alugar_mais = input()
        if alugar_mais == '2':
            break

def processo_devolver_item():
    '''
    Inicia o processo de devolução de um determinado item por parte do locador. O usuário digita o ID do item que ele deseja devolver. Se o ID corresponder ao de algum item que o locador tenha, ele será devolvido. O item então será marcado como disponível novamente.
    '''
    while True:
        id_item_a_devolver = input("Digite o id do item que quer devolver: ")
        
        for item in usuario_logado.get_itens_escolhidos():
            if item.get_ident() == int(id_item_a_devolver) and item.get_entregue() == True:
                item.set_entregue(False)
                item.set_alugado(False)
                item.set_disponivel(True)
                usuario_logado.get_itens_escolhidos().remove(item)

        for item in estoque.get_lista_itens():
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

def processo_confirmar_locacao():
    '''
    Inicia o processo de confirmar a locação do item. O usuário é perguntado, primeiramente, o id do item confirmado. Se o ID do item corresponder ao ID de algum dos itens que estão na lista de pagamentos pendentes do usuário, o pagamento será confirmado e o item será marcado como indisponível e alugado.
    '''
    while True:
        id_do_item_confirmado = input("Digite o id do item confirmado: ")
        confirmou = False
        for item in usuario_logado.get_itens_escolhidos():
            if item.get_ident() == int(id_do_item_confirmado) and item.get_alugado() == False:
                item.set_alugado(True)
                confirmou = True
                break
        for item in estoque.get_lista_itens():
            if item.get_ident() == int(id_do_item_confirmado) and item.get_alugado() == False:
                item.set_alugado(True)
                break
        if confirmou == True:
            print("Item confirmado! Deseja alugar outro?")
            alugar_outro = input("[1] Sim \n[2] Não")
            if alugar_outro == '2':
                break

def processo_cadastrar_item():
    '''
    Realiza o processo de cadastrar item, pedindo informações sobre ele (nome e preco) e chamando o estoque para cadastrá-lo nele.
    '''
    nome = input('Nome do item: ')
    preco = input('preco: ')
    estoque.cadastrar_item(nome, float(preco), True, False, False, usuario_logado)
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
        print(f'Bem vindo, {usuario_logado.get_nome()}.')
            
        if usuario_logado.get_tipo() == 1:
            while True:
                print("O que deseja fazer?")
                print("[1] Alugar itens \n[2] Ver lista de itens que já chegaram \n[3] Pagar itens alugados \n[4] Sair")
                o_que_fazer = input()
                
                if o_que_fazer == '1':
                    processo_locacao()
                elif o_que_fazer == '2':
                    print("Esses são os itens que já chegaram")
                    for item in usuario_logado.get_itens_escolhidos():
                        if item.get_entregue() == True:
                            print(item)

                    print("Deseja devolver algum item?")
                    print("[1] Sim \n[2] Não")
                    devovler = input()
                    if devovler == '1':
                        processo_devolver_item()
                elif o_que_fazer == '3':
                    print("Esses são os itens pendentes:")
                    for item in usuario_logado.get_itens_escolhidos():
                        if item.get_alugado() == False:
                            print(item)           
                    processo_confirmar_locacao()
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
                    print('Esses são os itens que você tem disponíveis para exclusão: ')
                    for item in estoque.get_lista_itens():
                        if item.get_dono() == usuario_logado and item.get_alugado() == False and item.get_disponivel() == True:
                            print(item)
                    id = input('Digite o id do item que deseja excluir: ')

                    if estoque.excluir_item(int(id), usuario_logado) == True:
                        print('Item removido com sucesso!')
                    else:
                        print('Esse item não está cadastrado ou está locado.')
                elif opcao == '3':
                    print("Esses são os itens que você tem e que foram requisitados:")
                    tem_item_pra_enviar = False
                    for item in estoque.get_lista_itens():
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
                            if usuario_logado.enviar_itens(estoque) == True:
                                print("Itens enviados!")
                                for locador in locadores:
                                    for item in locador.get_itens_escolhidos():
                                        if item.get_disponivel() == False and item.get_alugado() == True and item.get_dono() == usuario_logado:
                                            item.set_entregue(True)
                            else:
                                print("Itens não puderam ser enviados")
                elif opcao == '4':
                    usuario_logado = None
                    break

print("Obrigado por utilizar o nosso programa!")

    