import psycopg2
from accounts.models.customer import Customer

class CustomerRepository():
    conn_string = "host='localhost' dbname='capstone' user='postgres' password='password123'"

    def insert(self, customer: Customer):
        with psycopg2.connect(self.conn_string) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO customer 
                        (FirstName, LastName, AddressID, Email) VALUES
                        (%(first_name)s, %(last_name)s, %(address_id)s, %(email_address)s)
                        RETURNING id
                    """, {
                            'first_name': customer.first_name, 
                            'last_name': customer.last_name, 
                            'address_id': customer.address.id, 
                            'email_address': customer.email_address
                        }
                )
                customer.id = cursor.fetchone()[0]
        return customer

    # def get_by_id(self, id):
    #     with psycopg.connect(self.conn_string) as db:
    #         cursor = db.cursor()
    #         cursor.execute('SELECT ID, FIRST_NAME, LAST_NAME, ADDRESS_ID, EMAIL_ADDRESS FROM CUSTOMER WHERE ID=?;', [id])
    #     row = cursor.fetchone()
    #     address = self.address_repository.get_by_id(row[3])
    #     return Customer(id=row[0], first_name=row[1], last_name=row[2], address=address, email_address=row[4])

    # def get_all(self):
    #     results = []
    #     with psycopg.connect(self.conn_string) as db:
    #         cursor = db.cursor()
    #         cursor.execute('SELECT ID, FIRST_NAME, LAST_NAME, ADDRESS_ID, EMAIL_ADDRESS FROM CUSTOMER;')
    #     rows = cursor.fetchall()
    #     for row in rows:
    #         address = self.address_repository.get_by_id(row[3])
    #         results.append(Customer(id=row[0], first_name=row[1], last_name=row[2], address=address, email_address=row[4]))
    #     return results

    # def update(self, id, customer: Customer):
    #     if id != customer.id:
    #         return False
    #     if not self.address_repository.update(customer.address.id, customer.address):
    #         return False
    #     with psycopg.connect(self.conn_string) as db:
    #         db.execute('UPDATE CUSTOMER SET FIRST_NAME=?, LAST_NAME=?, ADDRESS_ID=?, EMAIL_ADDRESS=? \
    #             WHERE ID=?;', [customer.first_name, customer.last_name, customer.address.id, customer.email_address, id])

    # def delete(self, id):
    #     customer = self.get_by_id(id)
    #     if not self.address_repository.delete(customer.address.id):
    #         return False
    #     with psycopg.connect(self.conn_string) as db:
    #         db.execute('DELETE FROM CUSTOMER WHERE ID=?;', [id])
