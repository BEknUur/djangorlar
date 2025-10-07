from decouple import config 

ENV_POSSIBLE_OPTIONS = { 
    "local",
    "prod"
}

ENV_ID=config("DJANGORLAR_ENV_ID", default="local", cast=str)


SECRET_KEY = 'django-insecure-ofg$pclmub4vbisx)@1a=p3dv+xqd#u4jidp14a))(%bwx2d6u'
