import psycopg2
from accounts.models.address import Address

class AddressRepository():
    conn_string = "host='localhost' dbname='capstone' user='postgres' password='password123'"

    def insert(self, address: Address) -> Address:
        with psycopg2.connect(self.conn_string) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO address 
                        (Address, City, State, ZipCode) VALUES
                        (%(address)s, %(city)s, %(state)s, %(zip_code)s)
                        RETURNING id
                    """, {
                            'address': address.address, 
                            'city': address.city, 
                            'state': address.state, 
                            'zip_code': address.zip_code
                        }
                )
                address.id = cursor.fetchone()[0]
        return address
        
    # def get_by_id(self, id):
    #     with psycopg.connect(self.conn_string) as db:
    #         cursor = db.cursor()
    #         cursor.execute('SELECT ID, ADDRESS, CITY, STATE, ZIP_CODE FROM ADDRESS WHERE ID=?;', [id])
    #     row = cursor.fetchone()
    #     return Address(id=row[0], address=row[1], city=row[2], state=row[3], zip_code=row[4])

    # def get_all(self):
    #     results = []
    #     with psycopg.connect(self.conn_string) as db:
    #         cursor = db.cursor()
    #         cursor.execute('SELECT ID, ADDRESS, CITY, STATE, ZIP_CODE FROM ADDRESS;')
    #     rows = cursor.fetchall()
    #     for row in rows:
    #         results.append(Address(id=row[0], address=row[1], city=row[2], state=row[3], zip_code=row[4]))
    #     return results

    # def update(self, id, address: Address):
    #     if id != address.id:
    #         return False

    #     with psycopg.connect(self.conn_string) as db:
    #         db.execute('UPDATE ADDRESS SET ADDRESS=?, CITY=?, STATE=?, ZIP_CODE=? \
    #             WHERE ID=?;', [address.address, address.city, address.state, address.zip_code, id])

    # def delete(self, id):
    #     with psycopg.connect(self.conn_string) as db:
    #         db.execute('DELETE FROM ADDRESS WHERE ID=?;', [id])
