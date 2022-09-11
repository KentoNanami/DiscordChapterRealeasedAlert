import requests
from bs4 import BeautifulSoup
import pickle

url = "https://scantrad.net/one-punch-man"
s = requests.session()

current_scan, c = pickle.load(open("save.p", "rb"))


def discord_alert():
    url = "YOUR WEBHOOK"  # webhook url, from here: https://i.imgur.com/f9XnAew.png

    # for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    data = {"avatar_url": "https://dlmodfile.com/wp-content/uploads/2020/12/One-Punch-Man-Road-to-Hero-2.0.png",
            "username": "SAITAMA", "embeds": [
            {
                "color": 15158332,
                "description": "https://scantrad.net/mangas/one-punch-man/{}".format(c),
                "title": "Le chapitre {} de One-Punch-Man est sorti".format(c)

            }
        ]}

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
        c += 1
        current_scan = a
        print('Un nouveau scan de One Punch Man est disponible')
        discord_alert()
        pickle.dump([current_scan, c], open("save.p", "wb"))
    else:
        print('Pas de nouveau scan')
except:
    print('Fuck there is no wifi rn')


