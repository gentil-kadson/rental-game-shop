class Carrinho:
    def __init__(self, itens_pedido: list[itemPedido], usa_transportadora: bool, endereco_entrega: Endereco, endereco_devolucao: Endereco) -> None:
        self.__itens_pedido = itens_pedido
        self.__total = 0
        self.__usa_transportadora = usa_transportadora
        self.__pago = False
        self.__entregue = False
        self.__devolvido = False
        self.__endereco_entrega = endereco_entrega
        self.__endereco_devolucao = endereco_devolucao
    
    def get_itens_pedido(self) -> list[itemPedido]:
        return self.__itens_pedido
    
    def set_itens_pedido(self, itens_pedido: list[itemPedido]) -> None:
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

    def get_endereco_entrega(self) -> Endereco:
        return self.__endereco_entrega
    
    def set_endereco_entrega(self, endereco_entrega: Endereco) -> None:
        self.__endereco_entrega = endereco_entrega

    def get_endereco_devolucao(self) -> Endereco:
        return self.__endereco_devolucao
    
    def set_endereco_devolucao(self, endereco_devolucao: Endereco) -> None:
        self.__endereco_devolucao = endereco_devolucao