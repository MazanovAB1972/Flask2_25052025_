class Config:
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False    
    SERVER_NAME = "0.0.0.0"
    PORT = 4444

class DevelopmentConfig(Config):
    DEBUG = True    
    SERVER_NAME = "0.0.0.0" 
    PORT=3333   