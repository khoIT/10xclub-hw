import unittest
from File_Parser import parseSpecsFile


class TestParseSpecsFile(unittest.TestCase):
    def test_parse_specs_file(self):
        headers = parseSpecsFile('specs/testformat1.csv')
        self.assertEqual(["column name", "width", "datatype"])
if __name__ == '__main__':
    unittest.main()
