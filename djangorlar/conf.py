from decouple import config 

ENV_POSSIBLE_OPTIONS=(
    "local",
    "prod"

)
ENV_ID=config("DJANGORLAR_ENV_ID",cast=str)


SECRET_KEY ='django-insecure-_riq7zik3y!^s0jp8s1#z!jw@%#c(tbn9rg$rjh-yzz=^sdahw'