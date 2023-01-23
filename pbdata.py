import os
from datetime import datetime

import requests

pbkey = os.getenv('PBKEY')
mmkey = os.getenv('MMKEY')


class PowerBallData:

    def __init__(self):
        self.headers = {
            "X-RapidAPI-Key": pbkey,
            "X-RapidAPI-Host": "powerball.p.rapidapi.com"
        }
        self.date_start = '11-01-1997'
        self.date_end = datetime.now().strftime("%m-%d-%Y")
        self.url_between = f"https://powerball.p.rapidapi.com/BetweenDates/{self.date_start}/{self.date_end}"
        self.url_stats = "https://powerball.p.rapidapi.com/stats"

    def get_draws(self):
        response = requests.get(self.url, headers=self.headers)
        # print(response.text)
        return response.json()

    def get_between(self):
        response = requests.get(self.url_between, headers=self.headers)
        # print(response.text)
        return response.json()

    def get_stats(self):
        response = requests.get(self.url_stats, headers=self.headers)
        # print(response.text)
        return response.json()


class MegaMillionsData:

    def __init__(self):
        self.headers = {
            "X-RapidAPI-Key": mmkey,
            "X-RapidAPI-Host": "mega-millions.p.rapidapi.com"
        }
        self.date_start = '11-01-1990'
        self.date_end = datetime.now().strftime("%m-%d-%Y")
        self.url = f"https://mega-millions.p.rapidapi.com/BetweenDates/"
        self.url_between = f"https://mega-millions.p.rapidapi.com/BetweenDates/{self.date_start}/{self.date_end}"
        self.url_stats = "https://mega-millions.p.rapidapi.com/stats"

    def get_all(self):
        response = requests.get(self.url, headers=self.headers)
        # print(response.text)
        return response.json()

    def get_between(self):
        response = requests.get(self.url_between, headers=self.headers)
        # print(response.text)
        return response.json()

    def get_stats(self):
        response = requests.get(self.url_stats, headers=self.headers)
        # print(response.text)
        return response.json()


# # print(mmdata)
# # 10	25	41	44	50
#
# mmdata = MegaMillionsData().get_stats()
# pbdata = PowerBallData().get_stats()
#
#
# lotto = [pbdata, mmdata]
#
# for index, data in enumerate(lotto):
#     print()
#     print(data.get('data'))
#     if index == 0:
#         print(f'Powerball Number:')
#     else:
#         print(f'MegaMillions Numbers:')
#
#     whiteballoccurrences = data.get('data').get('whiteballoccurrences')
#
#     if data.get('data').get('powerballoccurrences'):
#         specialballoccurrences = data.get('data').get('powerballoccurrences')
#     else:
#         specialballoccurrences = data.get('data').get('megaBalloccurrences')
#
#     sorted_dict_wb = sorted(whiteballoccurrences.items(), key=lambda x: x[1], reverse=True)
#     sorted_dict_pb = sorted(specialballoccurrences.items(), key=lambda x: x[1], reverse=True)
#
#     print(f'Most occurring numbers:', end=' ')
#     numbers_list = []
#     for num in sorted_dict_wb[:5]:
#         numbers_list.append(int(num[0]))
#
#     for i in sorted(numbers_list):
#         print(i, end=' ')
#     print(f'[{sorted_dict_pb[:1][0][0]}]')
#     most = "21 32 61 63 69 24"
#
#     sorted_dict_wb = sorted(whiteballoccurrences.items(), key=lambda x: x[1], reverse=False)
#     sorted_dict_pb = sorted(specialballoccurrences.items(), key=lambda x: x[1], reverse=False)
#
#     print(f'Least occurring numbers:', end=' ')
#     numbers_list = []
#     for num in sorted_dict_wb[:5]:
#         numbers_list.append(int(num[0]))
#
#     for i in sorted(numbers_list):
#         print(i, end=' ')
#     print(f'[{sorted_dict_pb[:1][0][0]}]')
#     least = "4 13 26 34 49 15"


pbdata = PowerBallData().get_between()
mmdata = MegaMillionsData().get_between()

# 7	10 41 44 50 MegaMilly
# 3	8 9	39 44 PB
lotto = [pbdata, mmdata]

for index, data in enumerate(lotto):
    if index == 0:
        print(f'Powerball Number:')
    else:
        print(f'MegaMillions Numbers:')

    print(data)
    my_numbers = {
        0: [
            {
                'FirstNumber': 18,
                'SecondNumber': 22,
                'ThirdNumber': 37,
                'FourthNumber': 47,
                'FifthNumber': 54,
                'PowerBall': 36
            },
            {
                'FirstNumber': 21,
                'SecondNumber': 32,
                'ThirdNumber': 61,
                'FourthNumber': 63,
                'FifthNumber': 69,
                'PowerBall': 24
            },
            {
                'FirstNumber': 4,
                'SecondNumber': 13,
                'ThirdNumber': 26,
                'FourthNumber': 34,
                'FifthNumber': 49,
                'PowerBall': 15
            },
            {
                'FirstNumber': 3,
                'SecondNumber': 8,
                'ThirdNumber': 9,
                'FourthNumber': 39,
                'FifthNumber': 44,
                'PowerBall': 5
            },
            {
                'FirstNumber': 3,
                'SecondNumber': 8,
                'ThirdNumber': 9,
                'FourthNumber': 39,
                'FifthNumber': 50,
                'PowerBall': 7
            },
            {
                'FirstNumber': 3,
                'SecondNumber': 8,
                'ThirdNumber': 9,
                'FourthNumber': 39,
                'FifthNumber': 60,
                'PowerBall': 11
            },
        ],
        1: [
            {
                'FirstNumber': 7,
                'SecondNumber': 10,
                'ThirdNumber': 41,
                'FourthNumber': 44,
                'FifthNumber': 50,
                'MegaBall': 7
            },
            {
                'FirstNumber': 7,
                'SecondNumber': 10,
                'ThirdNumber': 41,
                'FourthNumber': 44,
                'FifthNumber': 64,
                'MegaBall': 25
            },
            {
                'FirstNumber': 7,
                'SecondNumber': 10,
                'ThirdNumber': 11,
                'FourthNumber': 41,
                'FifthNumber': 50,
                'MegaBall': 11
            },

        ],
    }

    numbers: list = list(data['data'])
    # print(f'Numbers: {numbers}')
    for draw in numbers:
        del draw['DrawingDate']
        draw_values = list(draw.values())[:6]
        for numset in my_numbers[index]:
            all_matched = []
            match = []
            matchpb = []
            mynumber_set = numset.values()
            for my_number in list(mynumber_set)[:5]:
                if my_number in list(draw_values)[:5]:
                    match.append(my_number)
                    # print(f'My set {mynumber_set}  => Match: {my_number} in {draw_values}')
            my_pb = list(mynumber_set)[-1]
            draw_pb = list(draw_values)[-1]
            if my_pb == draw_pb:
                matchpb.append(my_pb)
                # print(f'My set {mynumber_set}  => Match: {my_number} in {draw_values}')

            all_matched = match + matchpb
            if len(all_matched) == 6:
                print(
                    f'JACKPOT!!! Matched: {len(all_matched)} - {list(all_matched)} -- My set {list(mynumber_set)}  =>  Drawn: {list(draw_values)}')
            elif len(all_matched) >= 3:
                print(
                    f'Matched: {len(all_matched)} - {list(all_matched)} -- My set {list(mynumber_set)}  =>  Drawn: {list(draw_values)}')

        # if len(match) >= 3:
        #     print(
        #         f'Winner Matched = {match} - MyNumbers: {numset.values()} - {draw.get("DrawingDate")} - {draw.get("NumberSet")}')
        # else:
        #     print(f'Not a winner! \n')
