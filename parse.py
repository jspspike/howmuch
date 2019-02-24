import os
import requests
import json
from itertools import zip_longest
from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader(searchpath='./templates/'),
)

TBAKEY = json.load(open('key.json'))['key']


def make_rows(houston, detroit):
    houston = houston.items()
    detroit = detroit.items()

    return zip_longest(houston, detroit)


def parse():
    with open('entries.csv', 'r') as f:
        lines = iter(f.readlines())
    next(lines)

    houston = {}
    detroit = {}

    houston_total = 0.0
    detroit_total = 0.0

    for line in lines:
        data = line.split(',')
        if data[1] in houston:
            houston[data[1]]['amount'] += float(data[2])
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
            
            if (data[3].strip("\n") == "Houston"):
                houston[data[1]] = {
                    "name": response['nickname'],
                    "amount": float(data[2]),
                    "img": img
                }

                houston_total += houston[data[1]]["amount"]
            else:
                detroit[data[1]] = {
                    "name": response['nickname'],
                    "amount": float(data[2]),
                    "img": img
                }

                detroit_total += detroit[data[1]]["amount"]
            print("Entered:{} {} ({})".format(data[1], response['nickname'], data[3].strip("\n")))

    for key in houston:
        houston[key]["per"] = (houston_total - houston[key]["amount"]) * (1 / (houston[key]["amount"] + 1))
    for key in detroit:
        detroit[key]["per"] = (detroit_total - detroit[key]["amount"]) * (1 / (detroit[key]["amount"] + 1))

    houston["?"] = {
        "name": "New Team",
        "num": "",
        "per": houston_total,
        "img": "unknown.png"
    }
    detroit["?"] = {
        "name": "New Team",
        "num": "",
        "per": detroit_total,
        "img": "unknown.png"
    }

    template = env.get_template('index.html')
    template.stream(entries=make_rows(houston, detroit)).dump('index.html')


parse()
