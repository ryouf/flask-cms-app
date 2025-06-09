import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'storagecms119'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '67EvvivFih1BC1hQkurEK4n4ROZ/l4vmOFvdQpKbaFdT+g+6UGirXqbCvVMsGsNRYn5omgUZsyRW+ASt/SmxWA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms-serversql.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'ryouf'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Rr118555323&'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    ### Microsoft Authentication ###
    CLIENT_SECRET = 'aRy8Q~pq5C13ZNAyGlg66kLn-zV9ND5Tt6LiWbKj'
    CLIENT_ID = '62d4b6a2-653c-4236-a632-55aaf067699e'
    AUTHORITY = 'https://login.microsoftonline.com/common'
    REDIRECT_PATH = '/getAToken'
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"
    PREFERRED_URL_SCHEME = 'https'
