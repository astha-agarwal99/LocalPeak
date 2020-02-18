import unittest


def peak(lst):
    peak_num = None
    if len(lst) == 1:
        peak_num = lst[0]
    if len(lst) > 1:
        if lst[0] > lst[1]:
            peak_num = lst[0]
        else:
            peak_num = lst[1]
    return peak_num


class PeakTest(unittest.TestCase):

    def test_No_element_has_no_peak(self):
        self.assertEqual(None, peak([]))

    def test_Single_element_has_itself_as_a_peak(self):
        self.assertEqual(1, peak([1]))

    def test_Two_elements_has_greatest_as_a_peak(self):
        self.assertEqual(2, peak([1, 2]))


if __name__ == '__main__':
    unittest.main()
