import unittest
import os
import json
import pandas as pd

class TestingExercise2_09(unittest.TestCase):
    def setUp(self) -> None:
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(ROOT_DIR, '..', 'dtypes.json'), 'r') as jsonfile:
            self.dtyp = json.load(jsonfile)
        self.data = pd.read_csv(os.path.join(ROOT_DIR, '..', 'Datasets', 'earthquake_data.csv'),
                                dtype = self.dtyp)

    def test_counts(self):
        self.counts = self.data.injuries_description.value_counts(dropna = False).reset_index().sort_values(by = 'index')
        self.assertEqual(list(self.counts['injuries_description']), (list([666, 193, 347, 143, 4723])))

if __name__ == '__main__':
    unittest.main()