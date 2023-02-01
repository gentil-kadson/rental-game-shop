from locador import Locador
from endereco import Endereco

class Transportadora:

    def __init__(self, nome : str, endereco : Endereco, carrinhos : list[Locador.Carrinho]):
        self.__nome = nome
        self.endereco = endereco
        self.__carrinhos = [list[carrinhos] for carrinho in Locador.Carrinho]

    def get_nome(self) -> str:
            return self.__nome
        
    def set_nome(self, new_nome: str) -> None:
            self.__nome = new_nome
    
    def get__carrinhos(self) -> Locador.Carrinho:
        return self.__carrinhos

    def set__carrinhos(self, new_carrinhos: list[Locador.Carrinho]) -> None:
        self.__carrinhos = new_carrinhos

    def transportar(self, carrinho : Locador.Carrinho):
        print(carrinho.set_entregue(True)) # por enquanto...

    def __str__(self):
        return f'Nome: {self.__nome}'