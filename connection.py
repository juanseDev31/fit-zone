from dotenv import load_dotenv
import os
from mysql.connector import pooling
from mysql.connector import Error

load_dotenv()

class Connection:
    DATABASE = os.getenv('DB_NAME')
    USERNAME = os.getenv('DB_USER')
    PASSWORD = os.getenv('DB_PASSWORD')
    DB_PORT = os.getenv('DB_PORT', '3306')
    HOST = os.getenv('DB_HOST', 'localhost')
    POOL_SIZE = int(os.getenv('DB_POOL_SIZE', 5))
    POOL_NAME = os.getenv('DB_POOL_NAME', 'fit_zone_pool')

    pool = None
    @classmethod
    def get_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size= cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD
                )
                print(f'Pool name: {cls.pool.pool_name}')
                print(f'Pool size: {cls.pool.pool_size}')

                return cls.pool
            except Error as e:
                print(f'An error occurred while obtaining the pool {e}')

        else:
            return cls.pool

    @classmethod
    def get_connection1(cls):
        return cls.get_pool().get_connection()

    @classmethod
    def releaseConnection(cls,connection):
        connection.close()

