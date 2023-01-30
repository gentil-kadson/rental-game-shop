
class Endereco:
    def __init__(self, logradouro: str, cidade: str, estado: str, pais: str) -> None:
        self.__logradouro = logradouro
        self.__cidade = cidade
        self.__estado = estado
        self.__pais = pais

    def get_logradouro(self) -> str:
        return self.__logradouro
    
    def set_logradouro(self,logradouro) -> None:
        self.__logradouro = logradouro

    def get_cidade(self) -> str:
        return self.__cidade
    
    def set_cidade(self, cidade) -> None:
        self.__cidade = cidade

    def get_estado(self) -> str:
        return self.__estado

    def set_estado(self, estado) -> None:
        self.__estado = estado

    def get_pais(self) -> str:
        return self.__pais

    def set_pais(self, pais) -> None:
        self.__pais = pais

    def __str__(self) -> str :
        return (f'Logradouro: {self.__logradouro}\nCidade: {self.__cidade}\nEstado: {self.__estado} \n{self.__pais}')