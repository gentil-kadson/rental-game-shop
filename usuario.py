# VER TIPAGEM DO ATRIBUTO 'tipo', SE É INTEIRO MESMO
import abc

class Usuario(abc.ABC):
    def __init__(self, nome: str, cpf_ou_cnpj: str, tipo: int, email: str, senha: str, endereco) -> None:
        '''
        Inicializa a classe abstrata Usuario. Recebe, como um parâmetro, um nome, do tipo string; cpf_ou_cnpj, do tipo string; tipo, do tipo inteiro -- esse tipo vai depender de qual classe que herda de Usuario está sendo inicializada: 1 para a classe Locador, 2 para a classe Locatario; email, do tipo string; senha, do tipo string; e endereco, do tipo Endereco.
        '''
        self.__nome = nome
        self.__cpf_ou_cnpj = cpf_ou_cnpj
        self.__tipo = tipo
        self.__email = email
        self.__senha = senha
        self.__logado = False
        self.__endereco = endereco

    def logar(self, email, senha) -> bool:
        '''
        Loga o usuário no sistema. Recebe como parâmetros um email, do tipo string; e uma senha, do tipo string. Retorna True se as credenciais do usuário baterem com as passadas pelos parâmetros, False se não houver sincronização.
        '''
        if self.get_email() == email and self.get_senha() == senha:
            self.__logado = True
            return True
        else:
            return False

    @abc.abstractmethod
    def enviar_itens(self):
        '''
        Ou envia os itens para o locador que tiver pelo menos um item alugado -- caso seja chamada pelo locatário --, ou envia um item de volta para o locatário, caso essa função seja chamada pelo locador.
        '''
        pass

    def get_nome(self) -> str:
        '''
        Retorna o nome do usuario que chamar esta função.
        '''
        return self.__nome

    def set_nome(self, nome) -> None:
        '''
        Define um novo nome para o usuário. Recebe um novo nome, do tipo string, como parâmetro.
        '''
        self.__nome = nome

    def get_cpf_ou_cnpj(self) -> str:
        '''
        Retorna o CPF/CNPJ do usuário que chamar esta função.
        '''
        return self.__cpf_ou_cnpj

    def set_cpf_ou_cnpj(self, cpf_ou_cnpj) -> None:
        '''
        Define um novo CPF/CNPJ para o usuário que chamar esta função. Recebe um cpf/cnpj como parâmetro, que é do tipo string.
        '''
        self.__cpf_ou_cnpj = cpf_ou_cnpj

    def get_tipo(self) -> int:
        '''
        Retorna o tipo de usuário que está chamando a função (1 se for locador, 2 se for locatário).
        '''
        return self.__tipo

    def set_tipo(self, tipo) -> None:
        '''
        Define um novo tipo para o usuário. Recebe tipo, do tipo inteiro, como parâmetro.
        '''
        self.__tipo = tipo

    def get_email(self) -> str:
        '''
        Retorna o email do usuário que chamar esta função.
        '''
        return self.__email

    def set_email(self, email) -> None:
        '''
        Define um novo email para o usuário que chamar esta função. Recebe email como parâmetro, que é do tipo string.
        '''
        self.__email = email

    def get_senha(self) -> str:
        '''
        Retorna a senha do usuário que chamar a função.
        '''
        return self.__senha

    def set_senha(self, senha) -> None:
        '''
        Define uma nova senha para o usuário que chamar a função. Recebe senha, do tipo string, como parâmetro.
        '''
        self.__senha = senha

    def get_logado(self):
        '''
        Retorna True se o usuário estiver logado, False se ele não estiver.
        '''
        return self.__logado

    def get_endereco(self):
        '''
        Retorna o endereço do usuário. Ele irá retornar um endereço de memória para o objeto endereço associado ao usuário que chamar esta função.
        '''
        return self.__endereco

    def set_endereco(self, endereco) -> None:
        '''
        Define um novo endereço para o usuário que chamar a função. Recebe um endereco, do tipo Endereco, como parâmetro.
        '''
        self.__endereco = endereco

    def __str__(self) -> str:
        '''
        Retorna todas as informações possíveis sobre o usuário (todos os seus atributos) em forma de string.
        '''
        return (f"Usuário: {self.__nome}\nCPF/CNPJ: {self.__cpf_ou_cnpj}\nTipo: {self.__tipo}\nEmail: {self.__email}\nSenha: {self.__senha}\nEndereço: {self.__endereco} ")
