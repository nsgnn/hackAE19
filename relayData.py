import requests
import time


url = 'http://url.com'
waitTime = 5


def sendData(value):
    query = {'data': value}
    res = requests.post(url, data=query)
    return res.text

def main():
    while True:
        # Wait some given time
        time.sleep(waitTime)

        # Collect data from sensors

        # Send data along to server
        sendData()
