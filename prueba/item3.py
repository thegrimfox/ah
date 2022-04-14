class Car:

    def __init__(self, maker: str, model: str, year: int) -> None:
        """ en esta parte se hacen las declaraciones
        parametros
        marca : es un entero
            esto el ma marca del vehiculo
        modelo: es un entero
            esto el el modelo del vehiculo
        año: es un entero
            este es el año de fabricacion del vehiculo"""

        self.maker = maker
        self.model = model
        self.year = year

    def maker_and_model(self):
        """aqui es donde se piden los parametros
            y retorna la marca y el modelo"""

        return {'maker': maker, 'model': model}
