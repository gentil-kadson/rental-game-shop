from item import Item

class Estoque:
    def __init__(self, lista_itens: list[Item]):
        self.__lista_itens = lista_itens

    def get_lista_itens(self) -> list[Item]:
        return self.__lista_itens

    def set_lista_items(self, new_lista_itens: list[Item]):
        self.__lista_itens = new_lista_itens
    
    def cadastrar_item(self, nome: str, preco: float, disponivel: bool, alugado: bool, entregue: bool, dono) -> bool:
        new_item = Item(nome, preco, disponivel, alugado, entregue, dono)
        self.__lista_itens.append(new_item)
        return True

    def excluir_item(self, ident: int, dono) -> bool:
        for item in self.__lista_itens:
            if item.get_ident() == ident and item.get_dono() == dono:
                self.__lista_itens.remove(item)
                return True
        return False        