from connection import Connection
from customer import Customer


class Dao_customer:
    SELECT = 'SELECT * FROM customer'
    INSERT = 'INSERT INTO customer(name, last_name, membership) VALUES(%s, %s, %s)'
    UPDATE = 'UPDATE customer Set name=%s, last_name=%s, membership=%s WHERE id=%s'
    DELETE = 'DELETE FROM customer WHERE id=%s'

    @classmethod
    def select(cls):
        connection = None
        try:
            connection = Connection.get_connection1()
            cursor = connection.cursor()
            cursor.execute(cls.SELECT)
            records = cursor.fetchall()
            customers = []
            for record in records:
                customer = Customer(record[0],record[1],record[2],record[3])
                customers.append(customer)
            return customers

        except Exception as e:
            print(f'An error ocurred while selecting customers: {e}')
        finally:
            if connection is not None:
                cursor.close()
                Connection.releaseConnection(connection)

    @classmethod
    def insert(cls, customer):
        connection = None
        try:
            connection = Connection.get_connection1()
            cursor = connection.cursor()
            values = (customer._name,customer._last_name,customer._membership)
            cursor.execute(cls.INSERT,values)
            connection.commit()
            return cursor.rowcount
        except Exception as e:
            print((f'An a error ocurred while inserting customer: {e}'))
        finally:
            if connection is not None:
                cursor.close()
                Connection.releaseConnection(connection)

    @classmethod
    def update(cls,customer):
        connection = None
        try:
            connection = Connection.get_connection1()
            cursor = connection.cursor()
            values = (customer._name,customer._last_name,customer._membership,customer._id)
            cursor.execute(cls.UPDATE,values)
            connection.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'An a error ocurred while updating customer: {e}')
        finally:
            if connection is not None:
                cursor.close()
                Connection.releaseConnection(connection)

    @classmethod
    def delete(cls,customer):
        connection = None
        try:
            connection = Connection.get_connection1()
            cursor = connection.cursor()
            values = (customer._id,)
            cursor.execute(cls.DELETE,values)
            connection.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'An a error ocurred while deleting customer: {e}')
        finally:
            if connection is not None:
                cursor.close()
                Connection.releaseConnection(connection)


