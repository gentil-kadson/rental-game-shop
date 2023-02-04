# VER TIPAGEM DO ATRIBUTO 'tipo', SE É INTEIRO MESMO

class Usuario:
    def __init__(self, nome: str, cpf_ou_cnpj: str, tipo: int, email: str, senha: str, endereco) -> None:
        self.__nome = nome
        self.__cpf_ou_cnpj = cpf_ou_cnpj
        self.__tipo = tipo
        self.__email = email
        self.__senha = senha
        self.__logado = False
        self.__endereco = endereco

    """ 
        Método logar - autenticação do usuário; 
        Recebe email e senha como parâmetros;
        Retorna True se o usuário conseguir logar, caso contrário retorna False.    
    """

    def logar(self, email, senha):
        if self.get_email() == email and self.get_senha() == senha:
            self.__logado = True
            print("Usuário logado!")
        else:
            self.__logado = False
            print("Os dados estão incorretos. Tente novamente.")

    """
        Método enviar_itens - método abstrato que é implementado por Locador e Locatário
        Encaminha o(s) item/itens para a entrega
        Caso seja chamado pelo locador, realiza a devolução do item
        Caso seja chamado pelo locatário, realiza a entrega para empréstimo do item
    """

    # VER SE RECEBE O CARRINHO COMO PARÂMETRO MESMO. SE SIM, MUDAR NO DIAGRAMA
    def enviar_itens(self):
        # implementar aqui
        pass

    """ getters e setters """

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome) -> None:
        self.__nome = nome

    def get_cpf_ou_cnpj(self) -> str:
        return self.__cpf_ou_cnpj

    def set_cpf_ou_cnpj(self, cpf_ou_cnpj) -> None:
        self.__cpf_ou_cnpj = cpf_ou_cnpj

    def get_tipo(self) -> int:
        return self.__tipo

    def set_tipo(self, tipo) -> None:
        self.__tipo = tipo

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email) -> None:
        self.__email = email

    def get_senha(self) -> str:
        return self.__senha

    def set_senha(self, senha) -> None:
        self.__senha = senha

    def get_logado(self):
        return self.__logado

    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco) -> None:
        self.__endereco = endereco

    def __str__(self) -> str:
        return (f"Usuário: {self.__nome}\nCPF/CNPJ: {self.__cpf_ou_cnpj}\nTipo: {self.__tipo}\nEmail: {self.__email}\nSenha: {self.__senha}\nEndereço: {self.__endereco} ")
