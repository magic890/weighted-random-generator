import unittest
from RandomGen import RandomGen


class RandomGenTest(unittest.TestCase):

    def test_check_random_nums_and_probabilities(self):
        self.assertTrue(RandomGen._check_random_nums_and_probabilities([1, 2], [0.5, 0.5]))
        self.assertFalse(RandomGen._check_random_nums_and_probabilities([1, 2, 5], [0.5, 0.5]))
        self.assertFalse(RandomGen._check_random_nums_and_probabilities([1, 2], [0.3, 0.2, 0.5]))

    def test_check_probabilities(self):
        self.assertTrue(RandomGen._check_probabilities([0.5, 0.5]))
        self.assertTrue(RandomGen._check_probabilities([0.1, 0.1, 0.15, 0.4, 0.25]))
        self.assertTrue(RandomGen._check_probabilities([0.01, 0.3, 0.58, 0.1, 0.01]))
        self.assertFalse(RandomGen._check_probabilities([0.21, 0.3, 0.58, 0.1, 0.01]))
        self.assertFalse(RandomGen._check_probabilities([0.5, 0.55]))
        self.assertFalse(RandomGen._check_probabilities([1.0000000001]))
        self.assertFalse(RandomGen._check_probabilities([0.3, 0.2]))

    def test_sort_numbers_on_probabilities(self):
        n = [-1, 0, 1, 2, 3]
        p = [0.01, 0.3, 0.58, 0.1, 0.01]

        n_sorted, p_sorted = RandomGen._sort_numbers_on_probabilities(n, p)

        self.assertEqual(n_sorted, [-1, 3, 2, 0, 1], "Numbers not sorted according to their probability")
        self.assertEqual(p_sorted, [0.01, 0.01, 0.1, 0.3, 0.58], "Probability not sorted in ascending order")

    def test_next_num(self):
        n = [-1, 0, 1, 2, 3]
        p = [0.01, 0.3, 0.58, 0.1, 0.01]
        rg = RandomGen(n, p)

        self.assertIsNotNone(rg.next_num())

    def test_real_probabilities(self):
        n = [-1, 0, 1, 2, 3]
        p = [0.01, 0.3, 0.58, 0.1, 0.01]
        rg = RandomGen(n, p)
        iterations = 100
        max_probability_error = 0.30
        generated_nums = []

        for _ in range(iterations):
            generated_nums.append(rg.next_num())

        generated_nums_occurrences = dict(
            map(lambda x: (x, list(generated_nums).count(x) / (iterations * 1.000)), generated_nums)
        )
        nums_occurrences = dict(zip(n, p))

        print("Expected number probability: ")
        print(nums_occurrences)
        print("Generated number probability: ")
        print(generated_nums_occurrences)
        print("Max probability deviation allowed: ")
        print(max_probability_error)

        ok = True
        for k, v in nums_occurrences.items():
            if k in generated_nums_occurrences:
                if abs(generated_nums_occurrences[k] - v) > max_probability_error:
                    ok *= False

        self.assertTrue(ok, "Deviation from expected probability too much big")


if __name__ == '__main__':
    unittest.main()
