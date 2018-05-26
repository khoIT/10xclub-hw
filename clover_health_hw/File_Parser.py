
class FileSpec(object):
    def __init__(self, fileName, specs):
        # represent a table in db, contains list of ColumnSpec
        self.name = fileName
        self.specs = specs

class ColumnSpec(object):
    # contain information for one column in table
    def __init__(self, column_name, width, datatype):
        self.column_name = column_name
        self.width = width
        self.datatype = datatype

class DataRow(object):
    def __init__(self, ):


def parseSpecsFile(filePath):
    with open(filePath,'r') as sf:
        headers = sf.read().strip().split(',')
        return headers
def loadData():
    #0. read specs file from specs/ to create table schema
    # each file in specs denotes a filetype and a table schema
    parseSpecsFile('specs/testformat1.csv')

    #1. read data file from data/ to insert data into table
if __name__=="__main__":
    loadData():
