from os import environ


class Config:
    ######################### Global Configuration #########################

    ENV = environ.get("TOYBOX_AUTHZ_ENV", "production")

    DEBUG = int(environ.get("TOYBOX_AUTHZ_DEBUG", "0"))

    TESTING = int(environ.get("TOYBOX_AUTHZ_TESTING", "0"))

    SECRET_KEY = environ.get("TOYBOX_AUTHZ_SECRET_KEY", "HARD_STRONG_SECRET_KEY")

    JSONIFY_PRETTYPRINT_REGULAR = True

    TIMEZONE = environ.get("TOYBOX_AUTHZ_TIMEZONE", "Asia/Tehran")

    ######################## Database Configuration ########################

    SQLALCHEMY_DATABASE_URI = environ.get("TOYBOX_AUTHZ_DATABASE_URI", None)

    SQLALCHEMY_TRACK_MODIGICATIONS = DEBUG

    ########################## User Configuration ##########################

    USER_DEFAULT_EXPIRY_TIME = int(environ.get("TOYBOX_AUTHZ_USER_DEFAULT_EXPIRY_TIME", "365"))
    
    USER_DEFAULT_ROLE = environ.get("TOYBOX_AUTHZ_USER_DEFAULT_ROLE", "member")

    USER_DEFAULT_STATUS = int(environ.get("TOYBOX_AUTHZ_USER_DEFAULT_STATUS", "0"))