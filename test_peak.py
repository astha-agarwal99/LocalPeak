import unittest


def peak(lst):
    peak_num = None
    if len(lst) == 1:
        peak_num = lst[0]
    if len(lst) > 1:
        peak_num = 0
        counter = 0
        while counter != len(lst):
            if peak_num < lst[counter]:
                peak_num = lst[counter]
            counter += 1

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


if __name__ == '__main__':
    unittest.main()
