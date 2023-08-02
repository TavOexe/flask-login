class Config:
    SECRET_KEY = 'mysecretkey'

class DevelopmentConfig (Config):
    DEBUG = True
    DRIVER = 'ODBC Driver 17 for SQL Server'
    SERVER = 'gmanserver.database.windows.net'
    DATABASE = '$NAME'
    uid = '$USER'
    pwd = '$PASS'
  

    connection_string = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={uid};PWD={pwd}'
    

config = {
    'development': DevelopmentConfig,
}


