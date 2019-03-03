import requests
import time
import serial



url = 'https://dank.barber.catapult.bates.edu/update.php'
waitTime = 1                                     # In seconds

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

def serRead(ser_bytes):
        decoded_bytes = ser_bytes[0:len(ser_bytes) - 2].decode("utf-8")


        print(decoded_bytes)
        # Send data along to server

        #humidity(percent) temp(celsius) photo(integer) soilmstr(percent) pH(ph)
        datas = decoded_bytes.split(" ")

        humidity = datas[0] 
        sendData(0, "humidity", humidity)
        temp = datas[1]
        sendData(0, "temp", temp)
        light = datas[2]
        sendData(0, "light", light)
        soilmst = datas[3]
        sendData(0, "soilmst", soilmst)
        ph = datas[4]
        sendData(0, "ph", ph)


def main():

    #print(sendData(3, 'light', 6.7))
    si0 = serial.Serial('/dev/ttyUSB0')
    #si1 = serial.Serial('/dev/ttyACM1')
    #si2 = serial.Serial('/dev/ttyACM2')
    #si3 = serial.Serial('/dev/ttyACM3')

    serialinputs = [si0]

    while True:
        # Wait some given time
        #time.sleep(waitTime)

        # Collect data from sensors
        try:
            for serinput in serialinputs:
                serRead(serinput.readline())
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            break


if __name__ == '__main__':
    main()
