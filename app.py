import json

from flask import Flask, jsonify

app = Flask(__name__)
x = {}

# Todo 1: Returns % of players above a particular year.
#  Input could be any year for example, 1989.
#  All players born on or after 1989 should be
#  considered and the percentage should be calculated.
@app.route('/year/<int:year>')
def get_player_by_year(year):
    z = []
    year -= 1
    for dic in x.values():
        try:
            y = int('19' + dic['DOB'].rsplit('-', 1)[1])
        except:
            y = -1
        if year < y:
            z.append(dic)
    per = str(round(len(z) / len(x) * 100, 2))
    return jsonify({"player_percentage": per + "%"})


# Todo 2: Average age of players in the different teams.
@app.route('/avg-age')
def average_age():
    ans_dic = {}
    for dic in x.values():
        if dic['Country'] != "":
            y = int('19' + dic['DOB'].rsplit('-', 1)[1])
            if dic['Country'] in ans_dic:
                ans_dic[dic['Country']].append(2022 - y)
            else:
                ans_dic[dic['Country']] = [2022 - y]

    for k, v in ans_dic.items():
        ans_dic[k] = round(sum(v) / len(v), 2)

    return jsonify(ans_dic)


# Todo 3: Which country has the maximum number of left-hand batsmen.
@app.route('/left-hand')
def left_hand():
    ans_dic = {}
    for dic in x.values():
        if dic['Country'] != "":
            if dic['Batting_Hand'] == 'Left_Hand':
                v = ans_dic.get(dic['Country'], 0)
                ans_dic[dic['Country']] = v + 1

    k, v = max(ans_dic.items(), key=lambda k: k[1])
    return jsonify({k: v})

# Todo 4: List all the players whose Country is not identified in the dataset.
@app.route('/und-player')
def und_player():
    ls = []
    for dic in x.values():
        if dic['Country'] == "":
            ls.append(dic['Player_Name'])
    return jsonify(ls)


# Todo 5: List of all players in an input Country
@app.route('/country/<string:country>')
def get_player_by_country(country):
    ls = []
    for dic in x.values():
        if dic['Country'] == country:
            ls.append(dic['Player_Name'])
    return jsonify(ls)


def load_json():
    global x
    with open('static/player.json') as f:
        x = json.load(f)


load_json()

if __name__ == '__main__':
    app.run()
