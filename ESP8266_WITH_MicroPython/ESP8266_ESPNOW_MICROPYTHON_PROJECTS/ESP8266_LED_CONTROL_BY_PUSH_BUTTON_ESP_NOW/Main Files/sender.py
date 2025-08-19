from machine import Pin
import network
import espnow
import time

# ----------------------------
#  Wi-Fi Initialization (STA Mode)
# ----------------------------
sta = network.WLAN(network.STA_IF)   # Create a Wi-Fi station interface
sta.active(True)                     # Activate STA mode
sta.disconnect()                     # For ESP8266: disconnect from any AP (required before ESP-NOW)

# ----------------------------
#  ESP-NOW Initialization
# ----------------------------
esp = espnow.ESPNow()                # Create ESP-NOW instance
esp.active(True)                           # For ESP8266: initialize ESP-NOW

# ----------------------------
#  Add Peer (Receiver MAC)
# ----------------------------
peer = b'\xd8\xbf\xc0\x0ed\xe9'      # Replace with receiver's MAC address
esp.add_peer(peer)                   # Add peer device to send messages

# ----------------------------
#  Button Setup
# ----------------------------
# Using GPIO5 (D1 on NodeMCU) as input pin
# Pin is configured as INPUT with internal PULL-UP resistor
# Button must connect GPIO → GND when pressed (active-low)
button = Pin(5, Pin.IN, Pin.PULL_UP)

# ----------------------------
#  State Variables
# ----------------------------
led_state = 0                        # Store LED state (0 = OFF, 1 = ON)
last_press_time = 0                  # Track last button press for debouncing

print("Sender ready. Press the button to toggle LED.")

# ----------------------------
#  Main Loop
# ----------------------------
while True:
    if button.value() == 0:          # Button pressed (active-low → reads 0)
        # Debounce check → ensure 300ms gap between valid presses
        if time.ticks_diff(time.ticks_ms(), last_press_time) > 300:
            led_state = 1 - led_state   # Toggle LED state (0→1, 1→0)

            # Prepare message to send (convert int to string, then encode to bytes)
            msg = str(led_state).encode()

            # Send message via ESP-NOW to peer
            esp.send(peer, msg)

            # Print status to serial (visible only when USB connected)
            print("Sent:", "LED ON" if led_state else "LED OFF")

            # Update debounce timer
            last_press_time = time.ticks_ms()

    # Small delay to reduce CPU usage
    time.sleep_ms(20)

