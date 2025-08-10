import network        # Import network module to handle Wi-Fi functions
import espnow         # Import ESP-NOW library for peer-to-peer communication
from machine import Pin  # Import Pin class to control GPIO pins

# -------------------- Wi-Fi Setup --------------------
sta = network.WLAN(network.STA_IF)  # Create a WLAN object in Station mode (STA_IF)
sta.active(True)                    # Activate the Wi-Fi interface
sta.disconnect()                    # Disconnect from any router (only needed for ESP8266 to avoid interference)

# -------------------- ESP-NOW Setup --------------------
esp = espnow.ESPNow()     # Create an ESP-NOW object
esp.active(True)          # Activate ESP-NOW (ESP8266 uses .active(True), ESP32 uses .init())

# -------------------- LED Setup --------------------
led = Pin(2, Pin.OUT)     # Set GPIO2 (D4 on NodeMCU) as output for the LED
led.value(0)              # Turn LED OFF initially

print("Receiver ready...")  # Inform user that the receiver is running

# -------------------- Main Loop --------------------
while True:
    peer, msg = esp.recv()      # Receive data: returns (peer_mac, message)
    if msg is not None:         # If a message is received (not None)
        try:
            val = int(msg)      # Try converting received message to integer
            if val == 1:        # If message is '1'
                led.value(1)    # Turn LED ON
                print("LED ON") # Print status
            else:               # If message is not '1'
                led.value(0)    # Turn LED OFF
                print("LED OFF")# Print status
        except ValueError:      # If message cannot be converted to integer
            print("Invalid data received:", msg)  # Print error message
