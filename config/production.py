from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xcc\x1b\xde(\\\xa0r\xa7\x98`\xe8\xde\xa5\xc1\xb4\x02'