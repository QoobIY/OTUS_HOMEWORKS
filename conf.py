class Config():
    DEBUG = False
    # DATABASE_URI='products.sqlite'


class DevelopentConfig(Config):
    DEBUG = True
    SERVER_NAME = "127.0.0.1:8082"
