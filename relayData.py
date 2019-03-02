import requests
import time
import serial



url = 'http://url.com'
waitTime = 5                                     # In seconds



def sendData(value):
    query = {'data': value}
    res = requests.post(url, data=query)
    return res.text




def main():

    serialInput = serial.Serial('/dev/ttyACM0')  # This should be modified to accept data from serial input

    serialInput.flush()

    while True:
        # Wait some given time
        time.sleep(waitTime)

        # Collect data from sensors
        try:
            ser_bytes = serialInput.readline()
            decoded_bytes = float(ser_bytes[0:len(ser_bytes) - 2].decode("utf-8"))
            # Send data along to server
            sendData(decoded_bytes)

        except:
            print("Keyboard Interrupt")
            break