from settings.base  import * 

DEBUG= True 
ALLOWED_HOSTS=[ 
]

DATABASE={
    'default': {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME":  "db.sqlite3",
}

}