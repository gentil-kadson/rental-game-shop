from item import Item

class ItemPedido:
    def __init__(self, item: Item, quantidade: int) -> None:
        self.__item = item
        self.__quantidade = quantidade
    
    def get_item(self) -> str:
        return self.__item

    def set_item(self, novo_nome_item: Item) -> None:
        self.__item = Item(novo_nome_item)
    
    def get_quantidade(self) -> int:
        return self.__quantidade

    def set_quantidade(self, quantidade) -> None:
        self.__quantidade = quantidade

    def __str__(self) -> str:
        return (f'Item: {self.__item}\nQuantidade: {self.__quantidade}')
