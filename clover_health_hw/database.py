from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Column, Boolean, Integer, Text, Table


from File_Parser import TableSpec


# class TableSchema(Base):


class Database(object):
    def __init__(self, host, user, passwd, db):
        engine_creds = "mysql+mysqldb://{}:{}@{}:5432/{}".format(user, passwd, host, db)
        self.engine = create_engine(engine_creds)
        self.metadata = MetaData(self.engine)

    def column_generation(self, spec):
        mapping = {
            'Text': Column(Text(int(spec.width))),
            'Boolean': Column(Boolean),
            'Integer': Column(Integer)
        }
        return mapping.get(spec.datatype)

    def create_table(self, tableSpec):
        attr_dict = {'__tablename__': tableSpec.name,
                    'id': Column(Integer, primary_key=True)}
        for spec in tableSpec.specs:
            attr_dict[spec.column_name] = self.column_generation(spec)

        from sqlalchemy.ext.declarative import declarative_base
        Base = declarative_base()

        MyTableClass = type('MyTableClass', (Base,), attr_dict)

        # table = Table('Example', self.metadata,
        #       Column('id',Integer, primary_key=True),
        #       Column('name',Text))
        Base.metadata.create_all(self.engine)
        import pdb; pdb.set_trace()


        return query


    def finish_transactions(self):
        self.conn.close()
