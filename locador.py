from usuario import Usuario
from estoque import Estoque

class Locador(Usuario):
    def __init__(self, nome: str, cpf: str, tipo: int, email: str, senha: str, endereco, itens_escolhidos) -> None:
        super().__init__(nome, cpf, tipo, email, senha, endereco)
        self.__itens_escolhidos = itens_escolhidos
    
    def get_itens_escolhidos(self):
        return self.__itens_escolhidos
    
    def set_itens_escolhidos(self, itens_escolhidos):
        self.__itens_escolhidos = itens_escolhidos

    def enviar_itens(self, ident: int, estoque: Estoque):
        item_enviado = False
        for item in estoque.get_lista_itens():
            if item.get_ident() == ident and item.get_disponivel() == False and item.get_entregue() == True and item.get_alugado() == True:
                item.set_alugado(False)
                item.set_disponivel(True)
                item.set_entregue(False)
                item_enviado = True
        return item_enviado
            

    def adicionar_item(self, item) -> bool:
        self.set_itens_escolhidos([*self.__itens_escolhidos, item])
        return True
