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
    pass
    # -----------------------------------
    # End
    # -----------------------------------


def main():
    app()


if __name__ == '__main__':
    main()
