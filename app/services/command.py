from abc import ABC, abstractmethod


class TareaCommand(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def execute(self, model):
        pass

class Tarea(TareaCommand):
    def execute(self, model):
        for tarea in self.__tareas:
            tarea.execute(model)

    def __init__(self):
        self.__tareas = [] # Aca se añaden las tareas que queremos que se ejecuten

    def add_tarea(self, tarea: TareaCommand):
        self.__tareas.append(tarea)


