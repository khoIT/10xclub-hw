from File_Parser import parseSpecsFile, createTableSpec
from database import Database

def loadData():
    #0. read specs file from specs
    # each file in specs denotes a filetype and a table schema
    spec_list = parseSpecsFile('specs/testformat1.csv')
    table_spec = createTableSpec(spec_list)

    #1. create table with schema given by specs in spec_file

    #2. read data file from data/ to insert data into table
if __name__=="__main__":
    loadData()
