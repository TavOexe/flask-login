class Config:
    SECRET_KEY = 'mysecretkey'

class DevelopmentConfig (Config):
    DEBUG = True
    DRIVER = 'SQL Server'
    SERVER = 'DESKTOP-T3ER55E\SQLEXPRESS'
    DATABASE = 'inpelsadb'
    #uid = <username>
    #pwd = <password>
    connection_string = f"""DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;"""
    

config = {
    'development': DevelopmentConfig,
}