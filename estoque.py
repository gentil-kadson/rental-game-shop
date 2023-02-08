from itertools import count
class Estoque:
    class Item:
        iterator = count(start=1, step=1)
        def __init__(self, nome: str, preco: float, disponivel: bool, alugado: bool, entregue: bool, dono) -> None:
            '''
            Inicializa um objeto do tipo Item. Recebe como parâmetros: nome, do tipo string; preco, do tipo float; se o item está disponível ou não para ser alugado; se o item já foi alugado -- isso acontece quando o pagamento é confirmado; se o item já foi entregue ao locador que pediu os itens; e o dono do item, do tipo Locatario.
            '''
            self.__id = self.iterator.__next__()
            self.__nome = nome
            self.__preco = preco
            self.__disponivel = disponivel
            self.__dono = dono
            self.__alugado = alugado
            self.__entregue = entregue

        def get_ident(self) -> int:
            '''
            Retorna o ID do item que chamar esta função.
            '''
            return self.__id
        
        def set_ident(self, ident) -> None:
            '''
            Define um novo ID para o item. Recebe como parâmetro um identificador, do tipo inteiro.
            '''
            self.__id = ident

        def get_alugado(self) -> bool:
            '''
            Retorna True se o item que chama esta função já foi alugado.
            '''
            return self.__alugado
        
        def set_alugado(self, alugado: bool) -> None: 
            '''
            Define se o item já foi alugado ou não. Recebe como parâmetro alugado, do tipo booleano. O valor deve ser True seo item já tiver sido alugado ou False se ele ainda não estiver -- isso inclui pagamentos pendentes.
            '''
            self.__alugado = alugado

        def get_entregue(self) -> bool:
            '''
            Retorna True se o item que chama esta função já foi entregue ao locador que o alugou.
            '''
            return self.__entregue

        def set_entregue(self, entregue: bool) -> None:
            '''
            Define se o item que chama esta função já foi entregue ou não. Recebe como parâmetro entregue, do tipo booleano. O valor deve ser True se o item já tiver sido entregue e False se ainda não tiver.
            '''
            self.__entregue = entregue

        def get_disponivel(self) -> bool:
            '''
            Retorna True se o item que chama esta função estiver disponível para ser alugado.
            '''
            return self.__disponivel
        
        def set_disponivel(self, disponivel: bool) -> None:
            '''
            Define se o item está disponível ou não para ser alugado. Recebe como parâmetro disponivel, do tipo booleano. O valor deve ser True se o item estiver disponível para a locação; False caso não esteja.
            '''
            self.__disponivel = disponivel

        def get_nome(self) -> str:
            '''
            Retorna o nome do item que chamar esta função.
            '''
            return self.__nome

        def set_nome(self, nome) -> None:
            '''
            Define um novo nome para o item. Recebe como parâmetro nome, do tipo string.
            '''
            self.__nome = nome

        def get_preco(self) -> float:
            '''
            Retorna o preco do item que chamar esta função.
            '''
            return self.__preco

        def get_dono(self):
            '''
            Retorna o dono, do tipo Locatario, do item que chamar esta função.
            '''
            return self.__dono

        def set_dono(self, novo_dono) -> None:
            '''
            Define um novo dono para o item. Recebe como parâmetro um novo_dono, do tipo Locatario.
            '''
            self.__dono = novo_dono

        def __str__(self) -> str:
            '''
            Retorna informações gerais sobre o item (seus atributos).
            '''
            return (f'ID: {self.__id}\nNome do Item: {self.__nome}\nPreço do Item: {self.__preco}\nDono do Item: {self.__dono.get_nome()}')

    def __init__(self, lista_itens: list[Item]):
        '''
        Inicializa um objeto do tipo Estoque com uma lista de itens do tipo Item. Esses itens serão armazenados por todo o sistema, pois o estoque é como um banco de dados.
        '''
        self.__lista_itens = lista_itens

    def get_lista_itens(self) -> list[Item]:
        '''
        Retorna a lista de itens que estão armazenados no estoque.
        '''
        return self.__lista_itens

    def set_lista_items(self, new_lista_itens: list[Item]):
        '''
        Define uma nova lista de itens que substituirão os itens atuais que estão armazenados no estoque. Recebe, como um parâmetro, uma lista de itens nova do tipo Item.
        '''
        self.__lista_itens = new_lista_itens
    
    def cadastrar_item(self, nome: str, preco: float, disponivel: bool, alugado: bool, entregue: bool, dono) -> bool:
        '''
        Cadastra um novo item no estoque. Recebe como parâmetro o nome, do tipo string; o preço, do tipo float; se o item está disponível ou não para alguel; se o item já foi alugado ou não -- caso a confirmação do pagamento já tenha sido efetuada, este atributo retorna True; se o item já foi entregue à casa de quem o alugou; e o dono do item, que, por padrão, é quem o cadastra.
        '''
        new_item = self.Item(nome, preco, disponivel, alugado, entregue, dono)
        self.__lista_itens.append(new_item)
        return True

    def excluir_item(self, ident: int, dono) -> bool:
        '''
        Exclui um item do estoque. Leva, como parâmetro, um identificador do tipo inteiro, que corresponde ao ID do item armazenado no estoque; e o dono, que é quem está executando a ação de excluir o item -- o dono é do tipo Locatário.
        '''
        for item in self.__lista_itens:
            if item.get_ident() == ident and item.get_dono() == dono and item.get_disponivel() == True and item.get_alugado() == False:
                self.__lista_itens.remove(item)
                return True
        return False        