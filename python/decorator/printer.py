from abc import abstractmethod, ABC


class Printer(ABC):

    @staticmethod
    @abstractmethod
    def print(message) -> None:
        pass


class ConsolePrinter(Printer):

    @staticmethod
    def print(message) -> None:
        print(message)
