from itertools import count
class Estoque:

    class Item:
        iterator = count(start=1, step=1)
        def __init__(self, nome: str, preco: float, disponivel: bool, alugado: bool, entregue: bool, dono) -> None:
            self.__id = self.iterator.__next__()
            self.__nome = nome
            self.__preco = preco
            self.__disponivel = disponivel
            self.__dono = dono
            self.__alugado = alugado
            self.__entregue = entregue

        def get_ident(self) -> int:
            return self.__id
        
        def set_ident(self, ident) -> None:
            self.__id = ident

        def get_alugado(self) -> bool:
            return self.__alugado
        
        def set_alugado(self, alugado: bool) -> None: 
            self.__alugado = alugado

        def get_entregue(self) -> bool:
            return self.__entregue

        def set_entregue(self, entregue: bool) -> None:
            self.__entregue = entregue

        def get_disponivel(self) -> bool:
            return self.__disponivel
        
        def set_disponivel(self, disponivel: bool) -> None:
            self.__disponivel = disponivel

        def get_nome(self) -> str:
            return self.__nome

        def set_nome(self, nome) -> None:
            self.__nome = nome

        def get_preco(self) -> float:
            return self.__preco

        def get_dono(self):
            return self.__dono

        def set_dono(self, novo_dono) -> None:
            self.__dono = novo_dono

        def __str__(self) -> str:
            return (f'ID: {self.__id}\nNome do Item: {self.__nome}\nPreço do Item: {self.__preco}\nDono do Item: {self.__dono.get_nome()}')
    def __init__(self, lista_itens: list[Item]):
        self.__lista_itens = lista_itens

    def get_lista_itens(self) -> list[Item]:
        return self.__lista_itens

    def set_lista_items(self, new_lista_itens: list[Item]):
        self.__lista_itens = new_lista_itens
    
    def cadastrar_item(self, nome: str, preco: float, disponivel: bool, alugado: bool, entregue: bool, dono) -> bool:
        new_item = self.Item(nome, preco, disponivel, alugado, entregue, dono)
        self.__lista_itens.append(new_item)
        return True

    def excluir_item(self, ident: int, dono) -> bool:
        for item in self.__lista_itens:
            if item.get_ident() == ident and item.get_dono() == dono and item.get_disponivel() == True and item.get_alugado() == False:
                self.__lista_itens.remove(item)
                return True
        return False        