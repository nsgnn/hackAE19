import requests
import time
import serial



url = 'http://url.com'
waitTime = 5                                     # In seconds



def sendData(value):
    query = {'data': value}
    res = requests.post(url, data=query)
    return res.text


def serRead(serialinput1):
        ser_bytes = serialinput1.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes) - 2].decode("utf-8"))

        # Send data along to server
        sendData(decoded_bytes)


def main():
    serialinput1 = serial.Serial('/dev/ttyACM0')  # This should be modified to accept data from serial input
    serialinput1.flush()
    while True:
        # Wait some given time
        time.sleep(waitTime)

        # Collect data from sensors
        try:
            serRead(serialinput1)
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            break
