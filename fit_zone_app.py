from customer import Customer
from dao_customer import Dao_customer

print('*** ')
option = None
while option != 5:
    print('''
    Please choose an option:
    1. List customers
    2. Add a customer
    3. Modify a customer
    4. Delete a customer
    5. Exit
    ''')

    option = int(input('Please choose an option (1-5): '))
    if option == 1:
        customers = Dao_customer.select()
        print('\n*** Customer List: ***')
        for customer in customers:
            print(customer)
        print()
    elif option == 2:
        var_name = input('Write the name: ')
        var_last_name = input('Write the last name: ')
        var_membership = input('Write the membership: ')
        customer = Customer(name=var_name, last_name=var_last_name, membership=var_membership)
        inserted_customers = Dao_customer.insert(customer)
        print(f'Inserted customers: {inserted_customers}\n')
    elif option == 3:
        var_customer_id = int(input('Enter the customer Id to modify: '))
        var_name = input('Write the name: ')
        var_last_name = input('Write the last name: ')
        var_membership = input('Write the membership: ')
        customer = Customer(var_customer_id,var_name,var_last_name,var_membership)
        updated_customers = Dao_customer.update(customer)
        print(f'Updated customers: {updated_customers}\n')
    elif option == 4:
        var_customer_id = int(input('Enter the customer ID to delete: '))
        customer = Customer(id=var_customer_id)
        deleted_customers = Dao_customer.delete(customer)
        print(f'Deleted customers: {deleted_customers}\n')
else:
    print('We are exiting the application. Goodbye!')

