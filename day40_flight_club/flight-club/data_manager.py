import requests
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = 'https://api.sheety.co/.../flightDeals/prices'
        self.header = {
            'Authorization': 'Bearer ...'
        }

    def add_user(self, user_name, user_lname, user_email):
        # Добавляем пользователя в sheety
        users_enpoint = "https://api.sheety.co/.../flightDeals/users"
        header = {
            "Authorization": "Bearer ..."
        }
        query = {
            "user": {
                    "firstName": user_name,
                    "lastName": user_lname,
                    "email": user_email
            }
        }
        try:
            response = requests.post(url=users_enpoint, headers=header, json=query)
            print(response.json())
        except:
            print('Упс. Что-то пошло не так')
        else:
            print('Пользователь успешно добавлен.')

    # Getting info from Sheety
    def get_sheet(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.header)
        raw_data = response.json()
        formatted_data = raw_data['prices']
        print(raw_data)
        return formatted_data

    # Put IATA codes got from flight search to Sheets
    def put_iata(self, sheet_with_iata):
        for i in range(len(sheet_with_iata)):
            print('Putting Iata')
            endpoint = f'{self.sheety_endpoint}/{sheet_with_iata[i]["id"]}'
            new_data = {
                'price': {
                        'iataCode': sheet_with_iata[i]['iataCode']
                }
            }
            response = requests.put(url=endpoint, headers=self.header, json=new_data)
            print(response.text)
