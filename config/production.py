from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xb7r\xa4\xb3\xba\x17q\x071\xbe\xfa\xa2\x89\xb4/\xd0'