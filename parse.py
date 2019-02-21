import os
import requests
import json
from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader(searchpath='./template/'),
)

TBAKEY = json.load(open('key.json'))['key']


def parse():
    with open('entries.csv', 'r') as f:
        lines = iter(f.readlines())
    next(lines)

    entries = {}

    for line in lines:
        data = line.split(',')
        if data[1] in entries:
            entries[data[1]]['amount'] += float(data[2])
        else:
            files = [f for f in os.listdir('./img') if f.startswith(data[1])]
            if len(files) == 0:
                img = 'unknown.png'
            else:
                img = files[0]

            headers = {'X-TBA-Auth-Key': TBAKEY}
            url = 'https://www.thebluealliance.com/api/v3/team/frc' + data[1] + '/simple'

            response = requests.get(url, headers=headers)
            response = response.json()

            entries[data[1]] = {
                "name": response['nickname'],
                "num": data[1],
                "amount": float(data[2]),
                "img": img
            }
            print("Entered:{} {}".format(data[1], response['nickname']))

    template = env.get_template('index.html')
    template.stream(entries=entries).dump('index.html')


parse()
