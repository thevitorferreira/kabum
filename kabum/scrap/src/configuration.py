"""src.configuration
module that holds the app configuration"""
import os

MONGODB = {
    'user': os.getenv('MONGO_USER', 'database-acessor'),
    'password': os.getenv('MONGO_PASSWORD', ''),
    'host': os.getenv('MONGO_HOST', ''),
    'dbname': os.getenv('MONGO_DBNAME', ''),
    'mongouri': os.getenv('MONGO_URI', '')
}
KABUMLINKS = {
    'base_link' : os.getenv('BASE_LINK', 'https://www.kabum.com.br'),
    'books_page_link': os.getenv(
        'HARDWARE_PAGE_LINK',
        '/hardware'
    )
}
