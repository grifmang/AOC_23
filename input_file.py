import requests
requests.packages.urllib3.disable_warnings()

class GetInput():

    def __init__(self):
        self.headers = '53616c7465645f5f3c86879490310204bc85dcc251d4185f3429885cd79de28ab76e39227d873ffc4c076ce255981a445d631b975f73d7ac2cd7b57fd914c69f'
    
    def get_input(self, day):
        headers = {'session': self.headers}
        session = requests.Session()
        ins = session.get(f'https://adventofcode.com/2023/day/{day}/input', cookies=headers, verify=False)
        with open(f'day{day}.txt', 'w', newline='') as file:
            file.write(ins.text)