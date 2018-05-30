import unittest

from File_Parser import parseSpecsFile, createTableSpec, parseDataFile
from database import Database

class TestParseSpecsFile(unittest.TestCase):
    def test_parse_specs_file_should_parse_file_correctly(self):
        data = parseSpecsFile('specs/testformattesting.csv')
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

    def test_parse_data_file_should_parse_file_correctly_given_a_spec_file(self):
        specs = parseSpecsFile('specs/testformattesting.csv')
        table_spec = createTableSpec('test_spec', specs)
        db = Database("localhost", "root", "password", "cloverhealth")
        table_class = db.create_table(table_spec)

        data_file = parseDataFile('data/testformattesting_testing.txt', table_class, table_spec)
        self.assertEqual(len(data_file.rows), 2)
        self.assertEqual(data_file.rows[0].row, ['Khoi', 'Tran', 1, 123])
        self.assertEqual(data_file.rows[1].row, ['Alice', 'Wond', 0, 0])

if __name__ == '__main__':
    unittest.main()
