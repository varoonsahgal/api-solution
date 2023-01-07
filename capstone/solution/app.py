import uvicorn
from fastapi import FastAPI
from accounts.models.account import Account
from accounts.services.account import AccountService
from accounts.repositories.account import AccountRepository
from accounts.repositories.customer import CustomerRepository
from accounts.repositories.address import AddressRepository
from typing import List

app = FastAPI()
address_repository = AddressRepository()
customer_repository = CustomerRepository()
account_repository = AccountRepository()
account_service = AccountService(account_repository, customer_repository, address_repository)

@app.post('/api/accounts')
async def open_account(account: Account) -> Account:
    if account.current_balance < 25.0:
        raise ValueError('$25.00 minimum required on account opening')
    return account_service.open_account(account)

# @app.get('/api/accounts', response_model=List[Account])
# async def retrieve_accounts():
#     return account_repository.get_all()

# @app.get('/api/accounts/{id}')
# async def retrieve_account(id):
#     account = account_repository.get_by_id(id)
#     if account:
#         return account
#     else:
#         return {}

# @app.put('/api/accounts/{id}/deposit/{amount}')
# async def deposit(id, amount):
#     mod = float(amount)
#     if mod <= 0:
#         return { 'message': 'Invalid amount specified on depost' }
#     account = account_repository.get_by_id(id)
#     account.current_balance += mod
#     account_repository.update(id, account)
#     return { 'message': 'Deposit completed successfully' }

# @app.put('/api/accounts/{id}/withdraw/{amount}')
# async def withdraw(id, amount):
#     mod = float(amount)
#     if mod <= 0:
#         return { 'message': 'Invalid amount specified on withdrawal' }
#     account = account_repository.get_by_id(id)
#     if mod > account.current_balance:
#         return { 'message': 'Withdrawal not completed because of potential overdraw' }
#     account.current_balance -= mod
#     account_repository.update(id, account)
#     return { 'message': 'Withdrawal completed successfully' }

# @app.delete('/api/accounts/{id}/close')
# async def close_account(id):
#     account_repository.delete(id)
#     return { 'message': 'Account closed' }

if __name__ == "__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=8080,reload=True) #,timeout_keep_alive=3600,debug=True,workers=10)