import tareas.logger import Logger

class calulator():
    def __init__(self) -> None:
        self.log = Logger()

        @staticmethod
        def suma(self, a, b):
            self.log.log('calculator suma fue llamado')
            return a + b

        @staticmethod
        def resta(self, a, b):
            self.log.log('claculator resta fue llamado')
            return a - b
