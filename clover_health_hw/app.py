import os

from File_Parser import parseSpecsFile, createTableSpec
from database import Database

def loadData():
    # 0. read specs file from specs
    # each file in specs denotes a filetype and a table schema
    spec_dir = 'specs/'
    table_spec_list = []
    for file_name in os.listdir(spec_dir):
        file_path = spec_dir + file_name
        spec_list = parseSpecsFile(file_path)
        table_spec_list.append(createTableSpec(file_name, spec_list))

    # 1. create table with schema given by specs in table_spec
    # for first time usage, need to create cloverhealth db with credentials below
    db = Database("localhost", "root", "password", "cloverhealth")
    table_class_list = []
    for table_spec in table_spec_list:
        table_class_list.append(db.create_table(table_spec))

    # 2. read data file from data/ to insert data into table
    table_class = table_class_list[0]
    row = table_class(id=2, name="khoi", last_name="Tran", valid=1, count=3)
    db.insert_data(row)


if __name__=="__main__":
    loadData()
