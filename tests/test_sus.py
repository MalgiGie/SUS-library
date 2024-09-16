import unittest
from sus_lib.sus import calculate_grades, calculate_grade, grade_bar_chart, sus_value_histogram, calculate_sus_values, show_statistics

class TestSusLib(unittest.TestCase):

    def test_grade_from_sus_value(self):
        self.assertEqual(calculate_grade(50.0), 'F')
        self.assertEqual(calculate_grade(62.0), 'D')
        self.assertEqual(calculate_grade(70.0), 'C')
        self.assertEqual(calculate_grade(80.0), 'B')
        self.assertEqual(calculate_grade(90.0), 'A')

    def test_sus_values(self):
        answers = [[1, 4, 2, 4, 1, 4, 1, 4, 2, 5],
        [1, 4, 1, 3, 1, 4, 2, 4, 1, 5],
        [2, 5, 2, 5, 1, 5, 1, 5, 4, 2],
        [5, 1, 5, 1, 4, 1, 5, 1, 5, 1],
        [3, 4, 3, 4, 3, 4, 3, 4, 3, 4]]
        self.assertAlmostEqual(calculate_sus_values(answers[0]), 15.0)
        self.assertAlmostEqual(calculate_sus_values(answers[1]), 15.0)
        self.assertAlmostEqual(calculate_sus_values(answers[2]), 20.0)
        self.assertAlmostEqual(calculate_sus_values(answers[3]), 97.5)
        self.assertAlmostEqual(calculate_sus_values(answers[4]), 37.5)
        sus_values = calculate_sus_values(answers)
        self.assertAlmostEqual(sum(sus_values)/len(sus_values), 37.0)

    def test_import_from_csv(self):
        sus_values = calculate_sus_values('SUS-scores.csv')
        self.assertAlmostEqual(sum(sus_values)/len(sus_values),88.82352941176471)

if __name__ == '__main__':
    unittest.main()
