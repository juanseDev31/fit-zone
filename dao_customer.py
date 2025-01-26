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



if __name__ == '__main__':

    #insert
    customer1 = Customer(name='Alejandris',last_name='Tellez',membership='300')
    inserted_customers = Dao_customer.insert(customer1)
    print(f'Inserted customers: {inserted_customers}')

    #update
    # customer_to_update = Customer(3,'Alexa','Tellez',400)
    # updated_customers = Dao_customer.update(customer_to_update)
    # print(f'Updated customers: {updated_customers}')

    #delete
    # customer_to_delete = Customer(3)
    # deleted_customers = Dao_customer.delete(customer_to_delete)
    # print(f'Deleted customers: {deleted_customers}')


    customers = Dao_customer.select()
    for customer in customers:
        print(customer)

