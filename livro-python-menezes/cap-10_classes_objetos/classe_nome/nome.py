from functools import total_ordering


@total_ordering  # Implementa todos os operadores de comparação
class Nome:
    def __init__(self, nome):
        # if nome == None or not nome.strip():
        #     raise ValueError("Nome não pode ser nulo nem em branco.")
        self.nome = nome
        # self.chave = Nome.CriaChave(nome)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return f"<Classe {(type(self).__name__)} em 0x{id(self)} Nome: {self.__nome} Chave: {self.__chave}>"

    def __eq__(self, outro):
        # print("__eq__ Chamado")
        return self.nome == outro.nome

    def __lt__(self, outro):
        # print("__lt__ Chamado")
        return self.nome < outro.nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if valor == None or not valor.strip():
            raise ValueError("Nome não pode ser nul nem em branco")
        self.__nome = valor
        self.__chave = Nome.CriaChave(valor)

    @staticmethod  # Cria um método estático
    def CriaChave(nome):
        return nome.strip().lower()
