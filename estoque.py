from item import Item

# classe para salvar os items, usar arquivo.txt ou MySQL
class Estoque:

    def __init__(self):
        self.__lista_itens = list[Item]

    def get_lista_itens(self):
        return self.__lista_items

    def set_lista_items(self, new_lista_itens : list[Item]):
        self.__lista_itens = new_lista_itens