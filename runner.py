from pbdata import PowerBallData
from data_parser import DataParser
import json

data = PowerBallData().get_data()
op = DataParser(data).most_common_white_numbers()
pb = DataParser(data).most_common_pb_numbers()

# with open('../../Library/Application Support/JetBrains/PyCharm2022.2/scratches/pull.json', 'r') as t:
#     data = json.load(t)
# print(data)

mynumbers = [
    {
        'DrawingDate': '',
        'FirstNumber': 1,
        'SecondNumber': 2,
        'ThirdNumber': 3,
        'FourthNumber': 4,
        'FifthNumber': 5,
        'PowerBall': 24,
        'Multiplier': 0,
        'Jackpot': '',
        'NumberSet': ''
    }
]

compared = DataParser(data).compare_my_numbers(mynumbers)
