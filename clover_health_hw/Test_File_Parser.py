import unittest
from File_Parser import parseSpecsFile, createTableSpec


class TestParseSpecsFile(unittest.TestCase):
    def test_parse_specs_file_should_parse_file_correctly(self):
        data = parseSpecsFile('specs/testformat_nochange.csv')
        columns = [['name', '10', 'TEXT'], ['last_name', '4', 'TEXT'], ['valid', '1', 'BOOLEAN'], ['count', '3', 'INTEGER']]
        self.assertEqual(data, columns)

    def test_create_table_spec_create_correct_standard_spec(self):
        columns = [['name', '10', 'TEXT'], ['valid', '1', 'BOOLEAN'], ['count', '3', 'INTEGER']]
        tablespec = createTableSpec("test_file", columns)
        self.assertEqual(tablespec.name, "test_file")
        self.assertEqual(len(tablespec.specs), 3)
        specs = tablespec.specs
        self.assertEqual(specs[0].column_name, 'name')
        self.assertEqual(specs[0].width, 10)
        self.assertEqual(specs[0].datatype, 'Text')

if __name__ == '__main__':
    unittest.main()
