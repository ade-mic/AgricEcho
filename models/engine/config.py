#!/usr/bin/python3
import secrets
# Export environmental variables for MySQL database configuration
AGRICECHO_MYSQL_USER="agricecho_test"
AGRICECHO_MYSQL_PWD="agricecho_test_pwd"
AGRICECHO_MYSQL_HOST="localhost"
AGRICECHO_MYSQL_DB="agricecho_test_db"
# AGRICECHO_ENV='development'  # Or 'production' or 'test' depending on your environment

# echo "Environmental variables set:"
# echo "AGRICECHO_MYSQL_USER: $AGRICECHO_MYSQL_USER"
# echo "AGRICECHO_MYSQL_PWD: $AGRICECHO_MYSQL_PWD"
# echo "AGRICECHO_MYSQL_HOST: $AGRICECHO_MYSQL_HOST"
# echo "AGRICECHO_MYSQL_DB: $AGRICECHO_MYSQL_DB"
# echo "AGRICECHO_ENV: $AGRICECHO_ENV"

# Secret key for sqlachemy sessioon

SECRET_KEY = secrets.token_hex(16)
