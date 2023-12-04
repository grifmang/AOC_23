import requests
requests.packages.urllib3.disable_warnings()

class GetInput():

    def __init__(self):
        self.headers = ''
    
    def get_input(self, day):
        headers = {'session': self.headers}
        session = requests.Session()
        ins = session.get(f'https://adventofcode.com/2023/day/{day}/input', cookies=headers, verify=False)
        with open(f'day{day}.txt', 'w', newline='') as file:
            file.write(ins.text)
