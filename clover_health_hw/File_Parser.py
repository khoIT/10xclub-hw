
class TableSpec(object):
    def __init__(self, file_name, specs):
        # represent a table in db, contains list of ColumnSpec
        self.name = file_name
        self.specs = specs

class ColumnSpec(object):
    def __init__(self, column_name, width, datatype):
        # contain information for one column in table
        self.column_name = column_name
        self.width = width
        self.datatype = datatype.title()

class DataFile(object):
    def __init__(self, file_path, table_spec, rows):
        self.tableSpec = tableSpec
        self.row = rows

def parseDataFile(file_path, table_spec):
    columns = []
    with open(file_path,'r') as df:
        for line in df:
            columns.append(line.strip().split(' '))
    sf.close()
    return DataFile(file_path, table_spec, columns)

def parseSpecsFile(file_path):
    columns = []
    with open(file_path,'r') as sf:
        headers = sf.readline().strip().split(',')
        for line in sf:
            columns.append(line.strip().split(','))
    sf.close()
    return columns

def createTableSpec(file_name, specs_from_file):
    specs = []
    for row in specs_from_file:
        specs.append(ColumnSpec(row[0], row[1], row[2]))
    return TableSpec(file_name, specs)
