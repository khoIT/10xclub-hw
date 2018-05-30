from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Column, Boolean, Integer, Text, Table, String


class Database(object):
    def __init__(self, host, user, passwd, db):
        engine_creds = "mysql+mysqldb://{}:{}@{}:5432/{}".format(user, passwd, host, db)
        self.engine = create_engine(engine_creds)
        self.metadata = MetaData(self.engine)

    def __create_sqlalchemy_tableclass(self, table_spec):
        def column_generation(spec):
            mapping = {
                'Text': Column(String(int(spec.width))),
                'Boolean': Column(Boolean),
                'Integer': Column(Integer)
            }
            return mapping.get(spec.datatype)
        """
        allow dynamic column to be added in this tableClass as long as column type is
        valid in mapping dictionary
        """
        attr_dict = {'__tablename__': table_spec.name,
                    'id': Column(Integer, primary_key=True)}
        for spec in table_spec.specs:
            attr_dict[spec.column_name] = column_generation(spec)

        # create class using inheritance from sqlalchemy.Base
        from sqlalchemy.ext.declarative import declarative_base
        Base = declarative_base()
        tableClass = type('specTableClass', (Base,), attr_dict)
        return tableClass

    def create_table(self, tableSpec):
        tableClass = self.__create_sqlalchemy_tableclass(tableSpec)

        # if table exists, drop it so that new scheme can be updated
        if self.engine.dialect.has_table(self.engine, tableSpec.name):
            self.drop_table(tableClass)

        # Base.metadata.create_all(self.engine)
        tableClass.__table__.create(self.engine)
        return tableClass

    def drop_table(self, tableClass):
        # TODO: delete table if file gets deleted from folder
        tableClass.__table__.drop(self.engine)

    def insert_row(self, table_row):
        from sqlalchemy.orm import sessionmaker
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.add(table_row)
        session.commit()

    def insert_data_file(self, data_file):
        columns = data_file.table_class.__table__.columns.keys()

        for dataRow in data_file.rows:
            attr_dict = {}

            idx = 1
            while idx < len(columns) and idx <= len(dataRow.row):
                attr_dict[columns[idx]] = dataRow.row[idx-1]
                idx += 1
            row = data_file.table_class(**attr_dict)
            self.insert_row(row)

    def finish_transactions(self):
        self.conn.close()
