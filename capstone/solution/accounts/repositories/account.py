import psycopg2
from accounts.models.account import Account
from accounts.models.customer import Customer

class AccountRepository():
    conn_string = "host='localhost' dbname='capstone' user='postgres' password='password123'"

    def insert(self, account: Account) -> Account:
        with psycopg2.connect(self.conn_string) as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO account 
                        (AccountNumber, CustomerID, CurrentBalance) VALUES
                        (%(account_number)s, %(customer_id)s, %(current_balance)s)
                        RETURNING id
                    """, {
                            'account_number': account.account_number, 
                            'customer_id': account.customer.id, 
                            'current_balance': account.current_balance
                        }
                )
                account.id = cursor.fetchone()[0]
        return account

    # def get_by_id(self, id) -> Account:
    #     with psycopg.connect(self.conn_string) as db:
    #         cursor = db.cursor()
    #         cursor.execute('SELECT ID, ACCOUNT_NUMBER, CUSTOMER_ID, CURRENT_BALANCE FROM ACCOUNT WHERE ID=?;', [id])
    #     row = cursor.fetchone()
    #     return Account(id=row[0], account_number=row[1], customer=Customer() current_balance=round(row[3], 2))

    # def get_all(self):
    #     results = []
    #     with psycopg.connect(self.conn_string) as db:
    #         cursor = db.cursor()
    #         cursor.execute('SELECT ID, ACCOUNT_NUMBER, CUSTOMER_ID, CURRENT_BALANCE FROM ACCOUNT;')
    #     rows = cursor.fetchall()
    #     for row in rows:
    #         customer = self.customer_repository.get_by_id(row[2])
    #         results.append(Account(id=row[0], account_number=row[1], customer=customer, current_balance=round(row[3], 2)))
    #     return results

    # def update(self, id, account: Account):
    #     if str(id) != str(account.id):
    #         return False
    #     if not self.customer_repository.update(account.customer.id, account.customer):
    #         return False
    #     with psycopg.connect(self.conn_string) as db:
    #         db.execute('UPDATE ACCOUNT SET ACCOUNT_NUMBER=?, CUSTOMER_ID=?, CURRENT_BALANCE=? \
    #             WHERE ID=?;', [account.account_number, account.customer.id, account.current_balance, id])

    # def delete(self, id):
    #     account = self.get_by_id(id)
    #     if not self.customer_repository.delete(account.customer.id):
    #         return False
    #     with psycopg.connect(self.conn_string) as db:
    #         db.execute('DELETE FROM ACCOUNT WHERE ID=?;', [id])
