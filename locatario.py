from usuario import Usuario
from item import Item
from locador import Carrinho

class Locatario(Usuario):
    list_itens_locatario = [] # por enquanto criei essa lista aqui...

    def __init__(self, usuario : Usuario):
        super().__init__(usuario.get_nome(), usuario.get_cpf_ou_cnpj(),
                         usuario.get_tipo(), usuario.get_email(), usuario.get_senha(),
                         usuario.get_endereco())

    def cadastrar_item(self, ident : int, nome : str, preco : float, disponivel : bool) -> Item:
        new_item = Item(ident, nome, preco, disponivel, self)
        self.list_itens_locatario.append(new_item)  # adicionar na lista
        return new_item

    def excluir_item(self, ident : int) -> None: # remover da lista
        for item in range(self.list_itens_locatario):
            if item.get_ident == ident:
                self.list_itens_locatario.remove(item)

    def enviar_itens(self, carrinho : Carrinho):
        carrinho.set_entregue(True)
        print("realizou a entrega do ", carrinho)

    def ver_itens(self):
        for item in range(self.list_itens_locatario):
            print(item.get_nome())

    def __str__(self):
        return f'Nome: {self.get_nome}\n'