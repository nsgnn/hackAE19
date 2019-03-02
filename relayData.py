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
    si0 = serial.Serial('/dev/ttyACM0')
    si1 = serial.Serial('/dev/ttyACM1')
    si2 = serial.Serial('/dev/ttyACM2')
    si3 = serial.Serial('/dev/ttyACM3')

    serialinputs = [si0, si1, si2, si3]

    while True:
        # Wait some given time
        time.sleep(waitTime)

        # Collect data from sensors
        try:
            for serinput in serialinputs:
                serRead(serinput)
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            break
