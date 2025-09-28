def difference(*args):

    """
        Calculate the difference between the maximum and minimum of given numbers.

        :param args: int | float, any number of numeric arguments
        :return: float, difference between max and min values, rounded to 2 decimals; 0 if no arguments
        """

    if args:
        max_args = max(args)
        min_args = min(args)
        res_args = max_args - min_args
        return round( res_args, 2)
    else:
        return 0

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')