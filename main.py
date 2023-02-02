import json

from locador import Locador
from locatario import Locatario
from endereco import Endereco
from item import Item

locadores: list[Locador] = []
locatarios: list[Locatario] = []
criar_outra_conta: bool = True
usuario_logado: Locador | Locatario
logado: bool = False

def criar_conta():
    while criar_outra_conta == True:   
        print("Que tipo de conta quer criar?")
        print("[1] Locador\n [2] Locatário")
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

        if tipo_conta_a_criar == 1:
            print("Quer usar transportadora (você pode mudar depois)?")
            print("[1] Sim\n [2] Não")
            usa_transportadora = input()
            if usa_transportadora == 1:
                locador = Locador(True, endereco, endereco, nome, cpf_cnpj, 1, email, senha, endereco)
                locadores.append(locador)
            else:
                locador = Locador(False, endereco, endereco)
                locadores.append(locador)
        elif tipo_conta_a_criar == 2:
            locatario = Locatario(nome, 2, cpf_cnpj, email, senha, endereco)
            locatarios.append(locatario)
        
        print("Deseja criar outra conta?")
        print("[1] Sim [2] Não")
        opcao = input()
        if opcao == 2:
            criar_outra_conta == False

def logar():
    print("Que tipo de usuário é você?")
    print("[1] Locador\n [2] Locatário [3] Sair")
    opcao = input()
    if opcao == 3:
        print("Obrigado por utilizar nossa loja!")
    else:
        email_check = ("Digite o e-mail: ")
        senha_check = ("Digite a senha: ")
        if opcao == 1:
            for locador in locadores:
                if locador.get_email() == email_check and locador.get_senha() == senha_check:
                    usuario_logado = locador
                    logado = True
                    break
            
        if opcao == 2:
            for locatario in locatarios:
                if locatario.get_email() == email_check and locatario.get_senha() == senha_check:
                    usuario_logado = locatario
                    logado = True
                    break
        
        if logado == True:
            print("Bem-vindo à nossa loja!")
        else: 
            print("Usuário não existe.")

while logado == False:
    print("Bem-vindo ao Rental Game Shop!")
    print("Já tem conta?")
    print("[1] Sim\n [2] Não\n [3] Sair")
    ja_tem_conta = input()
    if ja_tem_conta == 1:
        while logado == False:
            logar()
    elif ja_tem_conta == 2:
        criar_conta()
    elif ja_tem_conta == 3:
        break

if logado == True:
    pass

opcao_cadastrar_item = input("Deseja cadastrar um item? [1] Sim \n [2] Não")
while opcao_cadastrar_item == 1:
    print("Cadastre seu item: ")
    ident = input("Código de identificação: ")
    nome = input("Nome: ")
    preco = ("Valor: ") 
    disponivel = input("O item estará disponível para locação? [1] Sim [2] Não")
    if disponivel == "1": 
        item = Item(ident, nome, preco, True, locatario)
    else:
        item = Item(ident, nome, preco, False, locatario)
    opcao_cadastrar_item = input("Deseja cadastrar um novo item? [1] Sim [2] Não")

    