
class TableSpec(object):
    def __init__(self, fileName, specs):
        # represent a table in db, contains list of ColumnSpec
        self.name = fileName.split('/')[1]
        self.specs = specs

class ColumnSpec(object):
    # contain information for one column in table
    def __init__(self, column_name, width, datatype):
        self.column_name = column_name
        self.width = width
        self.datatype = datatype.title()

class DataRow(object):
    def __init__(self, row):
        self.row = row


def parseSpecsFile(filePath):
    columns = []
    with open(filePath,'r') as sf:
        headers = sf.readline().strip().split(',')
        for line in sf:
            columns.append(line.strip().split(','))
        return columns

def createTableSpec(fileName, specsFromFile):
    specs = []
    for row in specsFromFile:
        spec = ColumnSpec(row[0], row[1], row[2])
        specs.append(spec)
    return TableSpec(fileName, specs)
