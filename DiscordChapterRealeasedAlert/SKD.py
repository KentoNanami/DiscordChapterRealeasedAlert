import requests
from bs4 import BeautifulSoup
import pickle


url = "https://scantrad.net/sakamoto-days"
s = requests.session()

current_scan = pickle.load(open("saveSKD.p", "rb"))


def discord_alert():
    url = "YOUR WEBHOOK"  # webhook url, from here: https://i.imgur.com/f9XnAew.png

    # for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    data = {
        "avatar_url" : "https://scan-trad.fr//content/310b86e0b62b828562fc91c7be5380a992b2786a/1606237391.png",
        "username": "Tarô Sakamoto"
            }

    data["embeds"] = [
        {
            "color": 15158332,
            "description": "https://scantrad.net/sakamoto-days",
            "title": "Un nouveau chapitre de Sakamoto Days est sorti"

        }
    ]

    result = requests.post(url, json=data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))

try:
    html = s.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    scan = soup.findAll('span', {'class': 'chl-num'})
    a = str(scan[0])
    if current_scan != a:
        current_scan = a
        print('Un nouveau scan de SKD est disponible')
        discord_alert()
        pickle.dump(current_scan, open("saveSKD.p", "wb"))
    else:
        print('Pas de nouveau scan')
except:
    print('Fuck there is no wi-fi rn')
