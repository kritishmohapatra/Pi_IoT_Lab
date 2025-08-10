from machine import Pin
import network
import espnow
import time

# Init Wi-Fi in STA mode
# Init Wi-Fi in STA mode
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.disconnect()  # Only for ESP8266

# Init ESP-NOW
esp = espnow.ESPNow()
esp.active(True)  # ESP8266

# Receiver's MAC address
peer = b'\xd8\xbf\xc0\x0ed\xe9'  # Change to your receiver MAC
esp.add_peer(peer)

# Button setup (active high with PULL_DOWN)
button = Pin(5, Pin.IN, Pin.PULL_UP)

led_state = 0
last_press_time = 0

#print("Sender ready. Press the button to toggle LED.")

while True:
    if button.value() == 0:  # Button pressed
        if time.ticks_diff(time.ticks_ms(), last_press_time) > 300:  # Debounce
            led_state = 1 - led_state  # Toggle
            msg = str(led_state).encode()
            esp.send(peer, msg)
            #print("Sent:", "LED ON" if led_state else "LED OFF")
            last_press_time = time.ticks_ms()
    time.sleep_ms(20)
