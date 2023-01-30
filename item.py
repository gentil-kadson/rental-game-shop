
class Item:
    def __init__(self, ident: int, nome: str, preco: float, disponível: bool, dono: Locatario) -> None:
        self.__id = ident
        self.__nome = nome
        self.__preco = preco
        self.__disponivel = False
        self.__dono = dono

    def get_ident(self) -> int:
        return self.__id

    def set_ident(self, ident) -> None:
        self.__id = ident

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome) -> None:
        self.__nome = nome

    def get_preco(self) -> float:
        return self.__preco

    def get_dono(self) -> str:
        return self.__dono

    def set_dono(self, novo_nome_dono) -> None:
        self.__dono = Locatario(novo_nome_dono)

    def __str__(self) -> str:
        return (f'ID: {self.__id}\nNome do Item: {self.__nome}\nPreço do Item: {self.__preco}\nDono do Item: {self.__dono}')
