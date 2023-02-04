from usuario import Usuario
from item import Item

class Locador(Usuario):
    # class Carrinho:
        # def __init__(self, itens_pedido: list[ItemPedido], usa_transportadora: bool, endereco_entrega, endereco_devolucao) -> None:
        #     self.__itens_pedido = itens_pedido
        #     self.__total = 0
        #     self.__usa_transportadora = usa_transportadora
        #     self.__pago = False
        #     self.__entregue = False
        #     self.__devolvido = False
        #     self.__endereco_entrega = endereco_entrega
        #     self.__endereco_devolucao = endereco_devolucao
        
        # def get_itens_pedido(self) -> list[ItemPedido]:
        #     return self.__itens_pedido
        
        # def set_itens_pedido(self, itens_pedido: list[ItemPedido]) -> None:
        #     self.__itens_pedido = itens_pedido
        
        # def get_total(self) -> float:
        #     return self.__total
        
        # def set_total(self, total: float) -> None:
        #     self.__total = total

        # def get_usa_transportadora(self) -> bool:
        #     return self.__usa_transportadora
        
        # def set_usa_transportadora(self, usa_transportadora: bool) -> None:
        #     self.__usa_transportadora = usa_transportadora

        # def get_pago(self) -> bool:
        #     return self.__pago
        
        # def set_pago(self, pago: bool) -> None:
        #     self.__pago = pago

        # def get_entregue(self) -> bool:
        #     return self.__entregue
        
        # def set_entregue(self, entregue: bool) -> None:
        #     self.__entregue = entregue

        # def get_devolvido(self) -> bool:
        #     return self.__devolvido
        
        # def set_devolvido(self, devolvido: bool) -> None:
        #     self.__devolvido = devolvido

        # def get_endereco_entrega(self):
        #     return self.__endereco_entrega
        
        # def set_endereco_entrega(self, endereco_entrega) -> None:
        #     self.__endereco_entrega = endereco_entrega

        # def get_endereco_devolucao(self):
        #     return self.__endereco_devolucao
        
        # def set_endereco_devolucao(self, endereco_devolucao) -> None:
        #     self.__endereco_devolucao = endereco_devolucao

    def __init__(self, nome: str, cpf: str, tipo: int, email: str, senha: str, endereco, itens_escolhidos: list[Item]) -> None:
        super().__init__(nome, cpf, tipo, email, senha, endereco)
        self.__itens_escolhidos = itens_escolhidos
    
    def get_itens_escolhidos(self) -> list[Item]:
        return self.__itens_escolhidos
    
    
    def set_itens_escolhidos(self, itens_escolhidos: list[Item]):
        self.__itens_escolhidos = itens_escolhidos
    
    def pagar_item_escolhido(self, id_item: int) -> bool:
        for item in self.__itens_escolhidos:
            if item.get_ident() == id_item:
                item.set_alugado(True)
                return True
            else:
                return False
    
    def get_itens_pagos(self) -> list[Item]:
        itens_pagos = []
        for item in self.__itens_escolhidos:
            if item.get_alugado() == True:
                itens_pagos.append(item)
        return itens_pagos
    
    def get_itens_entregues(self) -> list[Item]:
        itens_entregues = []
        for item in self.__itens_escolhidos:
            if item.get_entregue() == True:
                itens_entregues.append(item)
        return itens_entregues

    def adicionar_item(self, item: Item) -> bool:
        self.set_itens_escolhidos([*self.__itens_escolhidos, item])
        return True

    def remover_item(self, item: Item) -> bool:
        try:
            self.__itens_alugados.remove(item)
            return True
        except ValueError:
            return False
