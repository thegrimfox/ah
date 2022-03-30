import typer


app = typer.Typer()


class calculadora():
    def __init__(self) -> None:
        pass

    @staticmethod
    def suma(a, b):
        """
        in this part the sum of a and b will be done

        parameters
        -----
        a: int
            first number of the sum
        b: int
            the second number of the sum

        returns
        int
            the sum of a and b
        """
        return a + b

    @staticmethod
    def resta(a, b):
        """
        in this part the subtraction of a and b will be done


        parameters:
            a: int
                first number of the subtraction
            b:int
                second number of the subtraction
        returns
        int
            the subtraction of a and b
        """
        return a - b

    @staticmethod
    def division(a, b):
        """
        In this part, the division of a into b will be done


        parameters:
            a: int
                dividend
            b:int
                divider
        returns
        int
            the division between a and b
        """
        while b == 0:
            try:
                a / b
                break
            except ZeroDivisionError as e:
                return e

        return a/b

    @staticmethod
    def multiplicar(a, b):
        """
        In this part, the multiplication between a and b will be done

        parameters:
            a: int
                first number of the multiplication
            b:int
                second number of the multiplication
        returns
        int
            the multiplication of a and b
        """
        return a * b


@app.command()
def suma(a: int, b: int):
    res = calculadora.suma(a, b)
    print(f'la suma entre {a} y {b} es de {res}')


@app.command()
def resta(a: int, b: int):
    res = calculadora.resta(a, b)
    print(f'la resta entre {a} y {b} es de {res}')


@app.command()
def multiplicacion(a: int, b: int):
    res = calculadora.multiplicar(a, b)
    print(f'la multiplicacion entre {a} y {b} es de {res}')


@app.command()
def division(a: int, b: int):
    res = calculadora.division(a, b)
    print(f'la division entre {a} y {b} es de {res}')


def main():
    app()


if __name__ == '__main__':
    main()
