import machine
import dht
import time

sensor=dht.DHT11(machine.Pin(4))
while True:
    try:
        sensor.measure()
        temp=sensor.temperature()
        hum=sensor.humidity()
        print("Temp: {}°C  Humidity: {}%".format(temp, hum))
        time.sleep(2)
    except Exception as e:
        print("Error:-", e)