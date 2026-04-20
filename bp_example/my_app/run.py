import os,sys
sys.path.append(os.path.pardir)
from my_app import app
from my_app.config import ProductionConfig

print("\n ==== After loading config ====")
print(app.config)
app.config.from_object("my_app.config.DevelopmentConfig")

#if __name__=='__main__':
#  app.run(server_name=ProductionConfig.SERVER_NAME,
#          port=ProductionConfig.PORT,
#          debug=ProductionConfig.DEBUG)