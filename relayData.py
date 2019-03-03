import requests
import time
import serial



url = 'https://dank.barber.catapult.bates.edu/update.php'
waitTime = 5                                     # In seconds

def sendData(plant, sensor_type, value):
    epoch_time = int(time.time())
    query = {'time': epoch_time, 'plant_id': plant, 'type': sensor_type, 'value': value}
    print(query)
    try:
        res = requests.post(url, data=query)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print e
        sys.exit(1)


    return res.text

def serRead(serialInput):
        ser_bytes = serialInput.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes) - 2].decode("utf-8"))
        print(decoded_bytes)
        # Send data along to server
        # sendData(decoded_bytes)

def main():

    print(sendData(3, 'light', 6.7))
    # si0 = serial.Serial('/dev/ttyACM0')
    # si1 = serial.Serial('/dev/ttyACM1')
    # si2 = serial.Serial('/dev/ttyACM2')
    # si3 = serial.Serial('/dev/ttyACM3')

    # serialinputs = [si0, si1, si2, si3]

    # while True:
    #     # Wait some given time
    #     time.sleep(waitTime)

    #     # Collect data from sensors
    #     try:
    #         for serinput in serialinputs:
    #             serRead(serinput)
    #     except KeyboardInterrupt:
    #         print("Keyboard Interrupt")
    #         break


if __name__ == '__main__':
    main()
