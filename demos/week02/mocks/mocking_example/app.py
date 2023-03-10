from services.service import Service
from controllers.controller import Controller

def main():
    '''
    Launch point for application.
    '''

    quantity = int(input('Enter quantity: '))
    unit_cost = float(input('Enter unit cost: '))
    controller = Controller(Service())
    print("${:,.2f}".format(controller.get_discounted_price(quantity, unit_cost)))

if __name__ == "__main__":
    main()