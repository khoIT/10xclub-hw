import os

from File_Parser import parseSpecsFile, createTableSpec, parseDataFile
from database import Database

def loadData():
    # 0. read specs file from specs
    # each file in specs denotes a filetype and a table schema
    spec_dir = 'specs/'
    table_spec_list = {}
    for file_name in os.listdir(spec_dir):
        file_path = spec_dir + file_name
        spec_list = parseSpecsFile(file_path)
        table_spec_list[file_name.split('.')[0]] = createTableSpec(file_name, spec_list)

    # 1. create table with schema given by specs in table_spec
    # for first time usage, need to create cloverhealth db with credentials below
    db = Database("localhost", "root", "password", "cloverhealth")
    table_class_list = {}
    for name, table_spec in table_spec_list.iteritems():
        table_class_list[table_spec.name.split('.')[0]] = db.create_table(table_spec)

    # 2. read data file from data/ to insert data into table
    data_dir = 'data/'
    for file_name in os.listdir(data_dir):
        file_path = data_dir + file_name
        spec_file_name = file_name.split('_')[0]
        if spec_file_name not in table_class_list:
            print ("Couldn't find format file for {}".format(file_path))
            continue
        data_file = parseDataFile(file_path, table_class_list[spec_file_name], table_spec_list[spec_file_name])
        db.insert_data_file(data_file)

    # TODO: add test for loadData
if __name__=="__main__":
    loadData()
