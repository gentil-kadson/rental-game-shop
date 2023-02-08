from usuario import Usuario
from estoque import Estoque

class Locador(Usuario):
    def __init__(self, nome: str, cpf: str, tipo: int, email: str, senha: str, endereco, itens_escolhidos) -> None:
        '''
        Inicializa o objeto do tipo Locador, que herda de Usuário. Recebe um nome, do tipo string; um cpf, do tipo string; um tipo, do tipo inteiro -- este tipo será sempre igual a 1, já que o inicializador é da classe Locador; um e-mail, do tipo string; uma senha, do tipo string; um endereço do tipo Endereco; e itens escolhidos, que ou correspondem aos itens que ele pretende alugar, ou que estão pendentes em relação à confirmação do pagamento, ou os que já foram alugados.
        '''
        super().__init__(nome, cpf, tipo, email, senha, endereco)
        self.__itens_escolhidos = itens_escolhidos
    
    def get_itens_escolhidos(self):
        '''
        Retorna a lista de itens escolhidos pelo Locador para a locação.
        '''
        return self.__itens_escolhidos
    
    def set_itens_escolhidos(self, itens_escolhidos):
        '''
        Define uma nova lista de itens escolhidos para o Locador que chamar essa função. Recebe como parâmetro itens_escolhidos, que é uma lista do tipo Item.
        '''
        self.__itens_escolhidos = itens_escolhidos

    def enviar_itens(self, ident: int, estoque: Estoque):
        '''
        Envia um determinado item de volta para o Locatário. Recebe como parâmetro um identificador, do tipo inteiro; e um estoque, do tipo Estoque -- este corresponde a qual estoque o item está armazenado. Essa função só irá retornar True caso o item já tenha sido entregue ao usuário, caso o identificador encontre um item com ID correspondente e caso este item esteja no estoque que foi passado como parâmetro. No final, esse item volta a aparecer para o Locatário, já que foi devolvido.
        '''
        item_enviado = False
        for item in estoque.get_lista_itens():
            if item.get_ident() == ident and item.get_disponivel() == False and item.get_entregue() == True and item.get_alugado() == True:
                item.set_alugado(False)
                item.set_disponivel(True)
                item.set_entregue(False)
                item_enviado = True
        return item_enviado
            

    def adicionar_item(self, item) -> bool:
        '''
        Adiciona um item na coleção de itens_escolhidos do usuário. Recebe como parâmetro um item do tipo Item. Retorna True.
        '''
        self.set_itens_escolhidos([*self.__itens_escolhidos, item])
        return True
