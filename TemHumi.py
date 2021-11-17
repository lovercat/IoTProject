import Adafruit_HDT

sensor=Adafruit_HDT.DHT11

GPIO=24

humidity,temperature=Adafruit_HDT.read_retry(sensor,GPIO)

if(humidity is not None and temperature is not None):
    print(humidity)
    print(temperature)
