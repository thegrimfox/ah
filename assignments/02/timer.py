import time


def count_to(number=1000):
    for _ in range(number):
        time.sleep(0.001)


class Timer():

    def __init__(self, unit):
        """
        Constructor

        Parameters
        ----------
        unit : str
            Time unit [s|ms]
        """
        # -----------------------------
        # Add code here (start)
        # -----------------------------
        self.unit = unit
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
        # -----------------------------
        start = time.time()
        method()
        end = time.time()
        elapsed = end - start
        if self.unit == 's':
            return elapsed
        else:
            return elapsed * 1000
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
        # -----------------------------
        return self.unit
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
