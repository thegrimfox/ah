import typer
import time
from random import seed
from random import randint


app = typer.Typer()
seed(time.time())


def get_random_number(max_number: int = 100) -> int:
    """
    Generates a random number

    Parameters
    ----------
    max_number : int
       Maximun possible of the random number

    Returns
    -------
    int
        randon number
    """
    return randint(0, max_number)


@app.command()
def guess_the_number():
    """
    Guess number game
    """
    # -----------------------------------
    # Add your code here
    # -----------------------------------
    print('\n bienvenido al juego de disparos')
    print('\n las reglas son las siguientes:')
    print('\n 1)se dejara un blanco en un numero aleatorio')
    print('\n 2)usted tendra que colocar el numero de donde quiera disparar')
    print('\n 3) si le da gana')
    print('    si falla se indicara si el objetivo esta mas arriba o abajo')

    random = get_random_number()

    gun = int(input("introduzca una coordenada que crea ser la correcta\n"))
    print(f'su primera posicion es: \n{gun}')

    while gun != random:
        if(gun < random):
            print('\ntu objetivo esta mas arriba \n')
            gun = int(input('ingrese donde cree que este su objetivo \n'))
        else:
            print('\ntu objetivo esta mas abajo \n')
            gun = int(input('ingrese donde cree que este su objetivo\n'))
    print('\n le has dado a tu ojetivo')
    # -----------------------------------
    # End
    # -----------------------------------


def main():
    app()


if __name__ == '__main__':
    main()
