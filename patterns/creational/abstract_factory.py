class DBAccessEngine:

    def __init__(self, source):
        self.source = source
        self.engine = self.get_db_access_engine_instance()

    def get_db_access_engine_instance(self):
        if self.source == 'sql':
            return SqlDbAccessEngine()
        elif self.source == 'mongo':
            return MongoDbAccessEngine()
        else:
            raise ValueError(f'The source {self.source} is not supported yet.')

    def read_data(self, column):
        return self.engine.read_data(column)


class SqlDbAccessEngine:

    def __init__(self):
        self.host = 'localhost'
        self.port = 1234
        self.connection = None # CREATE MYSQL instance (sqlalchemy)

    def read_data(self, column):
        data = 'select query to select everthing from documenmt (table) ' \
               '"AGE" in mysql'
        return data


class MongoDbAccessEngine:

    def __init__(self):
        self.host = 'localhost'
        self.port = 9876
        self.connection = None # CREATE MONGODB instance (pymongo)

    def read_data(self, column):
        data = 'select query to select everything from table "AGE" in mysql'
        return data

def application_1():
    sql_object = DBAccessEngine('mongo')
    data = sql_object.read_data('age')
    return data

def application_2():
    sql_object = DBAccessEngine('sql')
    data = sql_object.read_data('age')
    return data

if __name__ == '__main__':

    print('Application 1: Gets data from MongoDB')
    print(f'Mongo Data {application_1()} \n')

    print('Application 2: Gets data from MySQL')
    print(f'Mongo Data {application_2()}')
