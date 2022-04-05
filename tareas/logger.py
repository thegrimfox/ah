class logger():
    def __init__(self, filename='log.txt') -> None:
        self.filename = filename
        self.f = self.open_if_neccesary()

    def open_if_neccesary(self):
        pass

    def log(self, msg):
        self.f.write(msg)
