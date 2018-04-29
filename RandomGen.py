import random
import functools
import bisect


class RandomGen(object):
    # Values that may be returned by next_num()
    _random_nums = []

    # Probability of the occurrences of random_nums
    _probabilities = []

    def __init__(self, random_nums, probabilities):

        # Every random number should has its respective probability
        if not self._check_random_nums_and_probabilities(random_nums, probabilities):
            raise ValueError("The number of random numbers to generate is not equal to the number of probabilities")

        # The sum of all the probabilities should be equal to 1
        if not self._check_probabilities(probabilities):
            raise ValueError("The sum of probabilities is not 1.0")

        # Probabilities should be sorted so the numbers
        self._random_nums, self._probabilities = self._sort_numbers_on_probabilities(random_nums, probabilities)

    @staticmethod
    def _check_random_nums_and_probabilities(random_nums, probabilities):
        """
        Check that every random number should has its respective probability.
        :param random_nums: Array of random numbers that may be returned.
        :param probabilities: Array of probabilities for the random numbers.
        :return: True if for every given number there is a probability, False otherwise.
        """
        return True if len(random_nums) == len(probabilities) else False

    @staticmethod
    def _check_probabilities(probabilities):
        """
        Check that the sum of all probabilities will be 1.0.
        :param probabilities: Array of probabilities.
        :return: True is the sum is 1.0, False otherwise.
        """
        return True if -1e-10 < functools.reduce(lambda x, y: x + y, probabilities) - 1.0 < 1e-10 else False

    @staticmethod
    def _sort_numbers_on_probabilities(_random_nums, _probabilities):
        """
        Sort probabilities in ascending order and the numbers according to this order.
        :param _random_nums: Array of random numbers that may be returned.
        :param _probabilities: Array of probabilities for the random numbers.
        :return: Tuple(_random_nums_sorted, _probabilities_sorted)
        """
        _pn = [[p, n] for p, n in sorted(zip(_probabilities, _random_nums))]
        return [item[1] for item in _pn], [item[0] for item in _pn]

    def next_num(self):
        """
        Returns one of the randomNums.
        When this method is called multiple times over a long period,
        it should return the numbers roughly with the initialized probabilities.
        """
        # To use bisect_left probabilities list should be sorted in ascending order
        return self._random_nums[bisect.bisect_left(self._probabilities, random.random()) - 1]
