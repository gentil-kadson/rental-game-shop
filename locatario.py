from usuario import Usuario
from endereco import Endereco
from estoque import Estoque


class Locatario(Usuario):
    def __init__(self, nome: str, tipo: int, cpf_ou_cnpj: str, email: str, senha: str, endereco: Endereco) -> None:
        '''
        Inicializa um objeto do tipo Locatario. Recebe um nome, do tipo string; um tipo, que é um inteiro -- esse valor sempre será igual a 2, já que está sendo passado para o inicializador de Locatario, que corresponde ao tipo 2 de Usuario; cpf_ou_cnpj, do tipo string; email, do tipo string; senha, do tipo string; e um endereço, que é do tipo Endereco.
        '''
        super().__init__(nome, cpf_ou_cnpj,
                         tipo, email, senha,
                         endereco)

    def enviar_itens(self, estoque: Estoque) -> bool:
        '''
        Envia todos os itens do estoque passado como parâmetro pertencentes ao locatário que estiver chamando essa função. Retorna True se pelo menos UM item foi enviado; False se não houver nenhum item para ser enviado. 
        '''
        entregou = False
        for item in estoque.get_lista_itens():
            if item.get_dono() == self and item.get_alugado() == True and item.get_disponivel() == False:
                item.set_entregue(True)
                entregou = True
        return entregou

    def __str__(self):
        return f'Nome: {self.get_nome}\n'