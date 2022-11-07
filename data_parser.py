from collections import OrderedDict


def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


class DataParser:

    def __init__(self, data: dict):
        self.data = data

    def most_common_white_numbers(self):
        list_dict = {
            'list_first': [],
            'list_second': [],
            'list_third': [],
            'list_fourth': [],
            'list_fifth': [],
            # 'list_pb': []
        }

        for draw in self.data['data']:
            list_dict['list_first'].append(draw['FirstNumber'])
            list_dict['list_second'].append(draw['SecondNumber'])
            list_dict['list_third'].append(draw['ThirdNumber'])
            list_dict['list_fourth'].append(draw['FourthNumber'])
            list_dict['list_fifth'].append(draw['FifthNumber'])
            # list_dict['list_pb'].append(draw['PowerBall'])

        final = []
        for lst in list_dict:
            for x in list_dict[lst]:
                dup = 0
                # print(x)
                if not final:
                    single_data = {
                        'number': x,
                        'occurrences': countX(list_dict[lst], x)
                    }
                    final.append(single_data)
                else:
                    for item in final:
                        # print(f'Item: {item}')
                        if x == item['number']:
                            dup += 1
                    if dup == 0:
                        single_data = {
                            'number': x,
                            'occurrences': countX(list_dict[lst], x)
                        }
                        final.append(single_data)
        # print('{} has occurred {} times'.format(x, countX(list_dict[lst], x)))
        dict1 = sorted(final, key=lambda d: d['occurrences'], reverse=True)
        print(f'White: {dict1[0:5]}')

    def most_common_pb_numbers(self):
        list_dict = {
            'list_pb': []
        }

        for draw in self.data['data']:
            list_dict['list_pb'].append(draw['PowerBall'])

        final = []
        for lst in list_dict:
            for x in list_dict[lst]:
                dup = 0
                # print(x)
                if not final:
                    single_data = {
                        'number': x,
                        'occurrences': countX(list_dict[lst], x)
                    }
                    final.append(single_data)
                else:
                    for item in final:
                        # print(f'Item: {item}')
                        if x == item['number']:
                            dup += 1
                    if dup == 0:
                        single_data = {
                            'number': x,
                            'occurrences': countX(list_dict[lst], x)
                        }
                        final.append(single_data)
        # print('{} has occurred {} times'.format(x, countX(list_dict[lst], x)))
        dict1 = sorted(final, key=lambda d: d['occurrences'], reverse=True)
        print(f'PB: {dict1[0]}')

    def compare_my_numbers(self, mynumbers: list):
        matched = {}
        count = 1

        res = [x for x in self.data['data'] + mynumbers if x not in self.data['data'] or x not in mynumbers]
        print(res)
