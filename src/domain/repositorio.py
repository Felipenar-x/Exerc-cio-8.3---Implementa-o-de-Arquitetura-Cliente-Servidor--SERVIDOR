from abc import ABC, abstractmethod

class ILivroRepository(ABC):
    @abstractmethod
    def obter_todos(self):
        pass

    @abstractmethod
    def obter_promocoes(self):
        pass

    @abstractmethod
    def obter_avaliacoes(self):
        pass
