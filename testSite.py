import requests


url = 'http://dankData.org'




def sendData(value):
    query = {'data': value}
    res = requests.post(url, data=query)
    return res.text

def main():
    ints = [123, 234, 345, 456]
    for i in ints:
        sendData(i)


if __name__ == '__main__':
    main()