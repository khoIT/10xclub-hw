import unittest

from File_Parser import TableSpec, ColumnSpec
from database import Database

class Test_Database(unittest.TestCase):
    def setUp(self):
        specs = [
            ColumnSpec('test_column_1','10','TEXT'),
            ColumnSpec('test_column_2','10','TEXT')
        ]
        self.table_spec = TableSpec('test_table',specs)
        # can set up a separate test db
        self.db = Database("localhost", "root", "password", "cloverhealth")

    def test_create_table_should_create_an_actual_table(self):
        table_class = self.db.create_table(self.table_spec)
        self.assertEqual(self.db.engine.dialect.has_table(self.db.engine, self.table_spec.name), True)

    def test_insert_should_put_a_record_into_test_table(self):
        table_class = self.db.create_table(self.table_spec)
        row = table_class(id=100, test_column_1="khoi", test_column_2="clover")
        self.db.insert_row(row)
        select_query = table_class.__table__.select()
        conn = self.db.engine.connect()

        data = conn.execute(select_query).fetchall()
        self.assertEqual(data, [((100, 'khoi', 'clover'))])
        conn.close()
if __name__ == '__main__':
    unittest.main()
