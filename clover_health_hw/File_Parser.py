class TableSpec(object):
    def __init__(self, file_name, column_specs):
        # represent a table in db, contains list of ColumnSpec
        self.name = file_name
        self.specs = column_specs

class ColumnSpec(object):
    def __init__(self, column_name, width, datatype):
        # contain information for one column in table
        self.column_name = column_name
        self.width = int(width)
        self.datatype = datatype.title()

class DataRow(object):
    def __init__(self, data_row, table_spec):
        # dynamically parse row data based on column_specs in table_spec
        row = self.__parse_row(data_row, table_spec)
        if not row:
            raise ValueError('Could not parse data_row')
        self.row = row

    def __parse_row(self, data_row, table_spec):
        idx = 0
        row = []
        if len(data_row) != len(table_spec.specs):
            print("Length of row and numbers of column don't match for table {} row {}".format(table_spec.name, data_row))
            return None

        while idx < len(table_spec.specs) and idx < len(data_row):
            spec = table_spec.specs[idx]
            data = data_row[idx]
            try:
                if spec.datatype == 'Boolean':
                    row.append(int(data))
                elif spec.datatype == 'Integer':
                    if len(data) > spec.width:
                        print("Length of data exceed column's width")
                        return None
                    row.append(int(data))
                elif spec.datatype == 'Text':
                    row.append(data)
                else:
                    print("Unrecognized data type: {}".format(spec.datatype))
                    return None
            except ValueError as err:
                print(err)
            idx += 1
        return row

class DataFile(object):
    def __init__(self, file_path, table_class, rows):
        self.table_class = table_class
        self.rows = rows

    def add_row(self, data_row):
        if type(data_row) == DataRow:
            self.rows.append(data_row)
        else:
            print("Can only work with DataRow type")

import csv

def parseDataFile(file_path, table_class, table_spec):
    rows = []
    with open(file_path,'r') as df:
        for line in csv.reader(df):
            try:
                data_row = DataRow(line[0].split(), table_spec)
            except ValueError as err:
                continue
            rows.append(data_row)
    df.close()
    return DataFile(file_path, table_class, rows)

def parseSpecsFile(file_path):
    columns = []
    with open(file_path,'r') as sf:
        reader = csv.reader(sf)
        headers = next(reader)
        for line in reader:
            columns.append(line)
    sf.close()
    return columns

def createTableSpec(file_name, specs_from_file):
    specs = []
    for row in specs_from_file:
        specs.append(ColumnSpec(row[0], row[1], row[2]))
    return TableSpec(file_name, specs)
