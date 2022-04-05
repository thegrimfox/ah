import typer
from tareas.calculator import Calculator
from logger import Logger

app = typer.Typer()
log = Logger('log.txt')
cal = Calculator()


@app.command()
def suma(a: int, b: int):
    log.log('CALCU suma fue llamado')
    res = cal.suma(a, b)
    print(f'suma de {a} y {b} es {res}')


@app.command()
def resta(a: int, b: int):
    log.log('CALCU resta fue llamado')
    res = cal.suma(a, b)
    print(f'resta de {a} y {b} es {res}')


def main():
    app()


if __name__ == '__main__':
    main()
