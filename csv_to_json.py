import csv
import json


def make_json(csv_path, json_path):
    data = {}
    with open(csv_path, encoding='utf-8-sig') as csvf:
        reader = csv.DictReader(csvf)
        for rows in reader:
            key = rows['Player_Name']
            data[key] = rows

    with open(json_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


if __name__ == '__main__':
    csv_path = r'static/Players.csv'
    json_path = r'static/player.json'
    make_json(csv_path, json_path)

