# import requests

# url = "https://newsdata.io/api/1/crypto?apikey=pub_f2a5595a428240b4b12e5989788c3f7c&q=crypto&sentiment=positive"

# print(url)

# r = requests.get(url)
# print(r.json())
# print(r.text())
# ----------------------------------------------------------------------------------------------------------------
import time
from plyer import notification

while True:
    print("Har Har Mahadev!")
    notification.notify(
        title = "Har Har Mahadev!",
        message = "Har Har Mahadev! Jai Bholenath!")
    time.sleep(5)
# ----------------------------------------------------------------------------------------------------------------
