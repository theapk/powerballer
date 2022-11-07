import os
from datetime import datetime

import requests

key = os.getenv('KEY')

class PowerBallData:

    def __init__(self):
        self.headers = {
            "X-RapidAPI-Key": key,
            "X-RapidAPI-Host": "powerball.p.rapidapi.com"
        }
        self.date_start = '11-01-1997'
        self.date_end = datetime.now().strftime("%m-%d-%Y")
        self.url = f"https://powerball.p.rapidapi.com/BetweenDates/{self.date_start}/{self.date_end}"

    def get_data(self):
        response = requests.get(self.url, headers=self.headers)
        # print(response.text)
        return response.json()
