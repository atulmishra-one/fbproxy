import os


class Base:
    DEBUG = True
    SECRET_KEY = r"\x0fj\x01\xee\xdc\x02G}\x86p\x9a\xc8\x93\xec[g+\xe7;\xa4R"
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Local(Base):
    SQLALCHEMY_DATABASE_URI = r"sqlite:///{}/data.db".format(Base.BASE_DIR)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(Local):
    pass


app_config = {
    'local': Local,
    'prod': Production
}