from decouple import config

# ENV _ID 

ENV_POSSIBLE_OPTIONS=(
    "local",
    "prod"
)


ENV_ID = config("DJANGORLAR_ENV_ID", cast=str)


SECRET_KEY = 'django-insecure-w8^uf02s5-evrgu%iyvf1!_yfkd(ia(98h_kp4pc7@m15bbjfx'



