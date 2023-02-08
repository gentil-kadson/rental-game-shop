
class Endereco:
    def __init__(self, logradouro: str, cidade: str, estado: str, pais: str) -> None:
        '''
        Inicialização da classe endereço. Recebe um logradouro, uma cidade, estado e pais
        '''
        self.__logradouro = logradouro
        self.__cidade = cidade
        self.__estado = estado
        self.__pais = pais

    def get_logradouro(self) -> str:
        '''
        Retorna o logradouro do determinado endereço.
        '''
        return self.__logradouro
    
    def set_logradouro(self,logradouro) -> None:
        '''
        Define um novo logradouro para o endereço que chama a função. Tem como parâmetro um logradouro do tipo string.
        '''
        self.__logradouro = logradouro

    def get_cidade(self) -> str:
        '''
        Retorna a cidade do enderço que chama a função.
        '''
        return self.__cidade
    
    def set_cidade(self, cidade) -> None:
        '''
        Define uma nova cidade para o endereço que chama esta função. Tem como parâmetro uma cidade, que é do tipo string.
        '''
        self.__cidade = cidade

    def get_estado(self) -> str:
        '''
        Retorna o estado a qual o endereço que chama a função pertence.
        '''
        return self.__estado

    def set_estado(self, estado) -> None:
        '''
        Define um novo estado para o endereço que chama esta função. Recebe como parâmetro um novo estado do tipo string.
        '''
        self.__estado = estado

    def get_pais(self) -> str:
        '''
        Retorna o país a qual pertence o endereço que chama esta função.
        '''
        return self.__pais

    def set_pais(self, pais) -> None:
        '''
        Define um novo país para o endereço que chamar essa função. Recebe como parâmetro um novo país do tipo string.
        '''
        self.__pais = pais

    def __str__(self) -> str:
        '''
        Retorna todas as informações possíveis sobre o endereço (todos os seus atributos).
        '''
        return (f'Logradouro: {self.__logradouro}\nCidade: {self.__cidade}\nEstado: {self.__estado} \n{self.__pais}')