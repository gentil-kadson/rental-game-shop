from usuario import Usuario
from endereco import Endereco
from estoque import Estoque


class Locatario(Usuario):
    def __init__(self, nome: str, tipo: int, cpf_ou_cnpj: str, email: str, senha: str, endereco: Endereco) -> None:
        super().__init__(nome, cpf_ou_cnpj,
                         tipo, email, senha,
                         endereco)

    def enviar_itens(self, estoque: Estoque) -> bool:
        entregou = False
        for item in estoque.get_lista_itens():
            if item.get_dono() == self and item.get_alugado() == True and item.get_disponivel() == False:
                item.set_entregue(True)
                entregou = True
        return entregou

    def __str__(self):
        return f'Nome: {self.get_nome}\n'