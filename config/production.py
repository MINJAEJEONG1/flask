from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xcf\xd4P\xff\xac\xaf\xc1\x11D\xca\xd3a\xd2\xbc/\x8f'