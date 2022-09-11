import requests
from bs4 import BeautifulSoup
import pickle


url = "https://scantrad.net/jujutsu-kaisen"
s = requests.session()

current_scan, c = pickle.load(open("saveJJK.p", "rb"))


def discord_alert():
    url = "YOUR WEBHOOK"  # webhook url, from here: https://i.imgur.com/f9XnAew.png

    # for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    data = {
        "avatar_url": "https://i.pinimg.com/564x/7a/bf/54/7abf54138ef6421e8ed5f6eabab30057.jpg",
        "username": "ITADORI YUJI"
            }

    data["embeds"] = [
        {
            "color": 15158332,
            "description": "https://scantrad.net/mangas/jujutsu-kaisen/{}".format(c),
            "title": "Le chapitre {} de Jujutsu Kaisen est sorti".format(c)

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
        c += 1
        print('Un nouveau scan de JJK est disponible')
        discord_alert()
        pickle.dump([current_scan, c], open("saveJJK.p", "wb"))
    else:
        print('Pas de nouveau scan')
except:
    print('Fuck there is no wi-fi rn')








