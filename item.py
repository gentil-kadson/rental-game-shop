from itertools import count

class Item:
    iterator = count(start=1, step=1)
    def __init__(self, nome: str, preco: float, disponivel: bool, dono, alugado: bool, devolvido: bool, entregue: bool) -> None:
        self.__id = self.iterator.__next__()
        self.__nome = nome
        self.__preco = preco
        self.__disponivel = disponivel
        self.__dono = dono
        self.__alugado = alugado
        self.__devolvido = devolvido
        self.__entregue = entregue

    def get_ident(self) -> int:
        return self.__id
    
    def set_ident(self, ident) -> None:
        self.__id = ident

    def get_alugado(self) -> bool:
        return self.__alugado
    
    def set_alugado(self, alugado: bool) -> None: 
        self.__alugado = alugado
    
    def get_devolvido(self) -> bool:
        return self.__devolvido
    
    def set_devolvido(self, devolvido: bool) -> None:
        self.__devolvido = devolvido

    def get_entregue(self) -> bool:
        self.__entregue

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

    def get_dono(self) -> str:
        return self.__dono

    def set_dono(self, novo_nome_dono) -> None:
        pass
        # self.__dono = Locatario(novo_nome_dono)

    def __str__(self) -> str:
        return (f'ID: {self.__id}\nNome do Item: {self.__nome}\nPreço do Item: {self.__preco}\nDono do Item: {self.__dono.get_nome()}')
