import requests
from functions import auth, logout, save_data

server = {"protocol": "https",
          "server": "kafe-new-habit.iiko.it",
          "port": "443",
          "date_for_ttk": "2024-10-18",
          "login": "reZon",
          "password": "RezonTheBest!"}
base_url = f'{server["protocol"]}://{server["server"]}:{server["port"]}/resto/api/'

if __name__ == '__main__':
    token = auth(login=server["login"],
                 password=server["password"],
                 server_data=server)
    data_type = ['Account', 'MeasureUnit', 'AccountingCategory', 'AlcoholClass', 'AllergenGroup',
                 'AttendanceType', 'Conception', 'CookingPlaceType', 'DiscountType', 'MeasureUnit',
                 'OrderType', 'PaymentType', 'ProductCategory', 'ProductScale', 'ProductSize',
                 'ScheduleType', 'TaxCategory']
    try:
        save_data(token, server, data_type="Products")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        logout(token, server)
