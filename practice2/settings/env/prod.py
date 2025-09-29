from settings.base  import * 

DEBUG= False 
ALLOWED_HOSTS=[ 
    "*"
]

DATABASE={
    'default': {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME":  "db.sqlite3",
}

}