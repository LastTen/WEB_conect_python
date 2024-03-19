import socketio

import os
from dotenv import load_dotenv

load_dotenv()

clanData = {
    "ReqId": 10,
    "Data": {
        "Title": "Tes23",
        "Description": "Retest1",
        "Type": 1,
        "MinLevel": 20,
        "PrefLang": "en",
        "Shield": 0,
        "Symbol": 0,
        "Pattern": 0,
        "Color": {
            "PatternColor": "#ffffff",
            "ShieldColor": "#ffffff",
            "SymbolColor": "#ffffff"
        }
    }
}


# standard Python
with socketio.SimpleClient() as sio:
    sio.connect(os.getenv('URL'), 
                headers= {'authorization': os.getenv('TOKEN')}, 
                transports=['websocket'])

    sio.emit('Clan/Create', clanData)

    event = sio.receive()
    print(f'received event: "{event[0]}" with arguments {event[1:]}')

print('stopping')


# print(os.getenv('URL'))