import network
import espnow
from machine import Pin

# Init Wi-Fi in STA mode
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()  # Only for ESP8266

# Init ESP-NOW
esp = espnow.ESPNow()
esp.active(True)  # <-- This works on ESP8266

# LED setup (GPIO2 = D4 on NodeMCU)
led = Pin(2, Pin.OUT)
led.value(0)  # Start OFF

print("Receiver ready...")

while True:
    peer, msg = esp.recv()
    if msg is not None:  # Ensure we got something
        try:
            val = int(msg)
            if val == 1:
                led.value(1)
                print("LED ON")
            else:
                led.value(0)
                print("LED OFF")
        except ValueError:
            print("Invalid data received:", msg)
