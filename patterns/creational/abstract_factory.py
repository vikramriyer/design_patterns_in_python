class DBAccessEngine:

    def __init__(self, source):
        self.source = source
        self.engine = self.get_db_access_engine_instance()

    def get_db_access_engine_instance(self):
        if self.source == 'sql':
            return SqlDbAccessEngine
        elif self.source == 'mongo':
            return MongoDbAccessEngine
        else:
            raise ValueError(f'The source {self.source} is not supported yet.')

    def read_data(self, column):
        self.engine.read_data(column)


class SqlDbAccessEngine:

    def __init__(self):
        self.host = 'localhost'
        self.port = 1234
        self.connection = None # create the sql db connection using sqlalchemy

    def read_data(self, column):
        data = f'select * from {column}'
        return data


class MongoDbAccessEngine:

    def __init__(self):
        self.host = 'localhost'
        self.port = 9876
        self.connection = None # create the mongo db connection using pymongo

    def read_data(self, column):
        data = db.collection.find()
        return data

if __name__ == '__main__':
    print('Got no errors. ')

# TODO 1: creating connections for respective dbs
# TODO 2: creating data manipulation common method to output same type of data