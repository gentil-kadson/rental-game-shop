from usuario import Usuario
from itemPedido import ItemPedido

class Locador(Usuario):
    class Carrinho:
        def __init__(self, itens_pedido: list[ItemPedido], usa_transportadora: bool, endereco_entrega, endereco_devolucao) -> None:
            self.__itens_pedido = itens_pedido
            self.__total = 0
            self.__usa_transportadora = usa_transportadora
            self.__pago = False
            self.__entregue = False
            self.__devolvido = False
            self.__endereco_entrega = endereco_entrega
            self.__endereco_devolucao = endereco_devolucao
        
        def get_itens_pedido(self) -> list[ItemPedido]:
            return self.__itens_pedido
        
        def set_itens_pedido(self, itens_pedido: list[ItemPedido]) -> None:
            self.__itens_pedido = itens_pedido
        
        def get_total(self) -> float:
            return self.__total
        
        def set_total(self, total: float) -> None:
            self.__total = total

        def get_usa_transportadora(self) -> bool:
            return self.__usa_transportadora
        
        def set_usa_transportadora(self, usa_transportadora: bool) -> None:
            self.__usa_transportadora = usa_transportadora

        def get_pago(self) -> bool:
            return self.__pago
        
        def set_pago(self, pago: bool) -> None:
            self.__pago = pago

        def get_entregue(self) -> bool:
            return self.__entregue
        
        def set_entregue(self, entregue: bool) -> None:
            self.__entregue = entregue

        def get_devolvido(self) -> bool:
            return self.__devolvido
        
        def set_devolvido(self, devolvido: bool) -> None:
            self.__devolvido = devolvido

        def get_endereco_entrega(self):
            return self.__endereco_entrega
        
        def set_endereco_entrega(self, endereco_entrega) -> None:
            self.__endereco_entrega = endereco_entrega

        def get_endereco_devolucao(self):
            return self.__endereco_devolucao
        
        def set_endereco_devolucao(self, endereco_devolucao) -> None:
            self.__endereco_devolucao = endereco_devolucao

    def __init__(self, usa_transportadora: bool, endereco_entrega, endereco_devolucao, nome: str, cpf: str, tipo: int, email: str, senha: str, endereco) -> None:
        super().__init__(nome, cpf, tipo, email, senha, endereco)
        self.__carrinho = self.Carrinho([], usa_transportadora, endereco_entrega, endereco_devolucao)
    
    def get_carrinho(self) -> Carrinho:
        return self.__carrinho
    
    def set_carrinho(self, carrinho: Carrinho) -> None:
        self.__carrinho = carrinho
    
    def pagar_carrinho(self) -> None:
        if self.__carrinho.get_pago() == False:
            self.__carrinho.set_pago(True)
            return True
        else:
            return False
    
    def adicionar_item(self, item, quantidade: int) -> bool:
        novo_item_pedido = ItemPedido(item, quantidade)
        self.__carrinho.set_itens_pedido(self.__carrinho.get_itens_pedido().append(novo_item_pedido))
        return True

    def remover_item(self, item: ItemPedido) -> bool:
        if item in self.__carrinho.get_itens_pedido():
            self.__carrinho.get_itens_pedido().remove(item)
            return True
        else:
            return False
