from machine import Pin      # Import Pin for GPIO (not actually used here, but can be used for buttons)
import network               # Import network module to handle Wi-Fi
import espnow                # Import ESP-NOW library for peer-to-peer communication

# -------------------- Wi-Fi Setup --------------------
sta = network.WLAN(network.STA_IF)  # Create a WLAN object in Station mode (STA_IF)
sta.active(True)                    # Activate the Wi-Fi interface
sta.disconnect()                    # Disconnect from any router (only needed for ESP8266 to avoid interference)

# -------------------- ESP-NOW Setup --------------------
esp = espnow.ESPNow()        # Create an ESP-NOW object
esp.active(True)             # Activate ESP-NOW (ESP8266 uses .active(True), ESP32 uses .init())

# -------------------- Peer (Receiver) Setup --------------------
peer = b'\xd8\xbf\xc0\x0ed\xe9'  # MAC address of the receiver (must match receiver's Wi-Fi MAC)
esp.add_peer(peer)               # Register the receiver as a peer in ESP-NOW

# -------------------- Main Loop --------------------
while True:
    try:
        # Get user input: 1 for LED ON, 0 for LED OFF
        val = int(input("Enter 1 to ON, 0 to OFF: "))
        
        # Convert the integer to string, then encode into bytes (ESP-NOW sends bytes)
        msg = str(val).encode()
        
        # Send the encoded message to the receiver
        esp.send(peer, msg)
        
        # Display status based on input
        if val == 1:
            print("LED ON command sent")
        else:
            print("LED OFF command sent")
    
    except ValueError:
        # If input is not 1 or 0, show error
        print("Please enter only 1 or 0")
