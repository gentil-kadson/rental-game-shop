from usuario import Usuario
from item import Item

class Locador(Usuario):
    def __init__(self, nome: str, cpf: str, tipo: int, email: str, senha: str, endereco, itens_escolhidos: list[Item]) -> None:
        super().__init__(nome, cpf, tipo, email, senha, endereco)
        self.__itens_escolhidos = itens_escolhidos
    
    def get_itens_escolhidos(self) -> list[Item]:
        return self.__itens_escolhidos
    
    def set_itens_escolhidos(self, itens_escolhidos: list[Item]):
        self.__itens_escolhidos = itens_escolhidos


    def adicionar_item(self, item: Item) -> bool:
        self.set_itens_escolhidos([*self.__itens_escolhidos, item])
        return True

    def remover_item(self, item: Item) -> bool:
        try:
            self.__itens_alugados.remove(item)
            return True
        except ValueError:
            return False
