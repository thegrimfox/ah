import typer


app = typer.Typer()


@app.command()
def suma(a: int, b: int):
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
    print(f'sum of a + b = {a+b}')

@app.command()
def resta(a: int, b: int):
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
    print(f'sustraction of a - b = {a-b}')

@app.command()
def division(a: int, b: int):
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
    print(f'division of a / b = {a/b}')

@app.command()
def multiplicar(a: int, b: int):
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
    print(f'multiplication of a * b = {a*b}')
def main():
    app()
    app()
    app()
    app()


if __name__ == '__main__':
    main()
