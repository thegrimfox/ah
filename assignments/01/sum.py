import typer


app = typer.Typer()


@app.command()
def suma(a: int, b: int):
    """
    this program makes the sum of a and b

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


def main():
    app()


if __name__ == '__main__':
    main()
