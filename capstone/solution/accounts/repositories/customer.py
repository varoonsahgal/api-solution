import psycopg2
from accounts.models.customer import Customer
from accounts.models.address import Address


class CustomerRepository():
    def insert(self, customer: Customer) -> Customer:
        with psycopg2.connect() as db:
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

    def get_by_id(self, id) -> Customer:
        with psycopg2.connect() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, FirstName, LastName, AddressID, Email FROM 
                        customer WHERE ID=%(customer_id)s
                    """, {
                    'customer_id': id
                }
                )
                row = cursor.fetchone()
        # In a larger enterprise app, you would likely be using an ORM like
        # SQLAlchemy, which would handle the mapping of the database row to the object
        # (and its hierarchy) automatically. The other approach you could take is to
        # use a separate set of DTOs (Data Transfer Objects) and manage mapping between
        # the DTO and the Pydantic model.
        return Customer.construct(id=row[0], first_name=row[1], last_name=row[2], address=Address.construct(id=row[3]), email_address=row[4])

    def delete(self, id) -> None:
        with psycopg2.connect() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM customer WHERE ID=%(customer_id)s
                    """, {
                    'customer_id': id
                }
                )
