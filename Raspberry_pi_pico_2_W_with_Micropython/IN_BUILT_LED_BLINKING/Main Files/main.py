import machine
import time

# Create an LED object for the onboard LED
# On the Raspberry Pi Pico 2 W, 'LED' maps to the built-in LED
led = machine.Pin("LED", machine.Pin.OUT)

# Infinite loop to blink the onboard LED
while True:
    led.value(1)    # Turn ON the LED
    time.sleep(1)   # Wait for 1 second
    
    led.value(0)    # Turn OFF the LED
    time.sleep(1)   # Wait for 1 second
