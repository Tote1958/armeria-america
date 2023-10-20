from abc import ABC, abstractmethod


class TareaCommand(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def execute(self):
        pass
