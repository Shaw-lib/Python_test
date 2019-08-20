# logger
BASE_LOG_DIR = os.path.join(BASE_DIR, "log")

LOGGING = {
    "version": 1, 
    "disable_existing_loggers": False, 
    "formatters": {
        "simple": {"format": "[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s"},
        "collect": {"format": "%(message)s"},
    },
    "filters": {"require_debug_true": {"()": "django.utils.log.RequireDebugTrue"}},
    "handlers": {
        # 终端
        "console": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        # 默认
        "default": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(BASE_LOG_DIR, "server_info.log"), 
            "maxBytes": 1024 * 1024 * 10, 
            "backupCount": 10, 
            "formatter": "simple",
            "encoding": "utf-8",
        },
        "error": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler", 
            "filename": os.path.join(BASE_LOG_DIR, "server_err.log"), 
            "maxBytes": 1024 * 1024 * 10, 
            "backupCount": 10,
            "formatter": "simple",
            "encoding": "utf-8",
        },
    },
    "loggers": {
        "": {"handlers": ["default"], "level": "INFO", "propagate": True},
        "error": {"handlers": ["error"], "level": "ERROR"},
        # overwrite
        "django.db.backends": {"handlers": ["console"], "level": "DEBUG"},
    },
}
