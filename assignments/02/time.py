import time
from tracemalloc import start, stop


def count_to(number=1000):
    for _ in range(number):
        time.sleep(0.001)


class Timer():

    def __init__(self, unit):
        
        # Constructor

        # Parameters
        # ----------
        unit = str
            Time.unit [s|ms]
        
        self.unit = unit
        self.method = method

        # -----------------------------
        # Add code here (start)

        start = time.time()

        # -----------------------------
        pass
        # -----------------------------
        # Add code here (end)
        # -----------------------------

    def measure_time(self, method):
        """
        Measure the time that takes to run a given method (function)

        Parameters
        ----------
        method : function
            Given method to measure

        Returns
        -------
        float
            The elapsed time in the unit from constructor 
        """
        # -----------------------------
        # Add code here (start)

        return self.method

        time.sleep(5.001)

        # measure_time

        return start-stop
        # -----------------------------
        pass
        # -----------------------------
        # Add code here (end)
        # -----------------------------

    def get_unit(self):
        """
        Returns the selected time measurement unit

        Returns
        -------
        str:
            Selected unit

        """
        # -----------------------------
        # Add code here (start)

        return self.unit

        stop = time.time()

        # -----------------------------
        pass
        # -----------------------------
        # Add code here (end)
        # -----------------------------


def main():
    t = Timer('ms')
    elapsed = t.measure_time(count_to)
    print(f'Elapsed time: {elapsed} {t.get_unit()}')
    t = Timer('s')
    elapsed = t.measure_time(count_to)
    print(f'Elapsed time: {elapsed} {t.get_unit()}')

if __name__ == '__main__':
    main()