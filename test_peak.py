import unittest


def peak(lst):
    peak_num = None

    if len(lst) > 0:
        peak_num = lst[0]
        counter = 1
        c = 0
        while counter != len(lst):
            if peak_num < lst[counter]:
                peak_num = lst[counter]
            else:
                c += 1

            counter += 1
            if c == 1:
                break

    return peak_num


class PeakTest(unittest.TestCase):

    def test_no_element_has_no_peak(self):
        self.assertEqual(None, peak([]))

    def test_single_element_has_itself_as_a_peak(self):
        self.assertEqual(1, peak([1]))

    def test_two_elements_has_greatest_as_a_peak(self):
        self.assertEqual(2, peak([1, 2]))

    def test_three_elements_has_peak_whose_left_and_right_are_smaller(self):
        self.assertEqual(5, peak([1, 5, 3]))

    def test_four_elements_has_peak_whose_left_and_right_are_smaller(self):
        self.assertEqual(9, peak([1, 5, 9, 3]))

    def test_four_elements_has_peak_whose_first_left_and_right_are_smaller(self):
        self.assertEqual(9, peak([1, 5, 9, 6, 15, 3]))

    def test_random_elements_peak(self):
        self.assertEqual(57, peak([1, 5, 9, 27, 32, 57, 43, 23, 6, 15, 3]))
    def test_array_with_same_elements(self):
        self.assertEqual(5, peak([5,5,5,5,5,5,5]))

if __name__ == '__main__':
    unittest.main()
