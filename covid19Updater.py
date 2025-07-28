import requests
from win10toast import ToastNotifier
import time
import json

def update():
    r = requests.get('https://disease.sh/v3/covid-19/countries/India')
    data = r.json()
    text = f'Confirmed Cases: {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'

    while True:
        toast = ToastNotifier()
        toast.show_toast("Covid-19 Updates", text, duration=20)
        time.sleep(60)

update()
