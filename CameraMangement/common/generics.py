#STATIC FILES
STATIC_FILE = "/staticfile"


ALPR_CODE='20230222000000000006'


DB={
  "default": {
    "ENGINE": "dj_db_conn_pool.backends.mysql",
    "NAME": "CAMERA_AI",
    "USER": "root",
    "PASSWORD": "Camera@12345",
    "HOST": "103.172.236.157",
    "PORT": "3306",
    "POOL_OPTIONS": {
      "POOL_SIZE": 20,
      "MAX_OVERFLOW": 50,
      "RECYCLE": 180
    }
  }
}
    
TOKEN_JWT= "qwjdkaasundasfnoasud8123123DA!@##!@$asdfd"

SECRET_SYSTEM_DEFAULT = "regfgfdgdf24324@#234_2fs#@$"
