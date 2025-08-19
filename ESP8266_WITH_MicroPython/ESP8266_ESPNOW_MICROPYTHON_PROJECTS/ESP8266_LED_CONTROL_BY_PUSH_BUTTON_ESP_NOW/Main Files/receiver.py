import network
import espnow
from machine import Pin

# ----------------------------
#  Wi-Fi Initialization (STA Mode)
# ----------------------------
sta = network.WLAN(network.STA_IF)   # Create Wi-Fi station interface
sta.active(True)                     # Enable station mode
sta.disconnect()                     # ESP8266 specific: disconnect from AP (needed before ESP-NOW)

# ----------------------------
#  ESP-NOW Initialization
# ----------------------------
esp = espnow.ESPNow()                # Create ESP-NOW instance
esp.active(True)                           # For ESP8266: initialize ESP-NOW (use .active(True) in some builds)

# ----------------------------
#  LED Setup
# ----------------------------
# Using GPIO2 (D4 on NodeMCU) as output LED pin
led = Pin(2, Pin.OUT)
led.value(0)                         # Ensure LED starts OFF

print("Receiver ready...")

# ----------------------------
#  Main Loop (Receive Data)
# ----------------------------
while True:
    peer, msg = esp.recv()           # Wait for data from sender (peer, message)
    if msg is not None:              # If valid message received
        try:
            val = int(msg)           # Convert message from bytes -> int (0 or 1)
            if val == 1:
                led.value(1)         # Turn LED ON
                print("LED ON")
            else:
                led.value(0)         # Turn LED OFF
                print("LED OFF")
        except ValueError:
            # If message is not an integer (unexpected data)
            print("Invalid data received:", msg)

