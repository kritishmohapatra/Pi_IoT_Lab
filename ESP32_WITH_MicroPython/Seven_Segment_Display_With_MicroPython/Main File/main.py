from machine import Pin
import time

# Configure 7-segment display pins (common cathode or common anode based on wiring)
# Each pin corresponds to one segment: a, b, c, d, e, f, g
led_a = Pin(21, Pin.OUT)
led_b = Pin(19, Pin.OUT)
led_c = Pin(17, Pin.OUT)
led_d = Pin(5, Pin.OUT)
led_e = Pin(18, Pin.OUT)
led_f = Pin(22, Pin.OUT)
led_g = Pin(23, Pin.OUT)

# ------------------------------
# Functions to display digits 0-9
# Each function turns ON/OFF the correct segments
# ------------------------------

def value_one():
    led_a.value(0)
    led_b.value(0)
    led_c.value(0)
    led_d.value(0)
    led_e.value(1)
    led_f.value(1)
    led_g.value(0)

def value_two():
    led_a.value(1)
    led_b.value(1)
    led_c.value(0)
    led_d.value(1)
    led_e.value(1)
    led_f.value(0)
    led_g.value(1)

def value_three():
    led_a.value(1)
    led_b.value(1)
    led_c.value(1)
    led_d.value(1)
    led_e.value(0)
    led_f.value(0)
    led_g.value(1)

def value_four():
    led_a.value(0)
    led_b.value(1)
    led_c.value(1)
    led_d.value(0)
    led_e.value(0)
    led_f.value(1)
    led_g.value(1)

def value_five():
    led_a.value(1)
    led_b.value(0)
    led_c.value(1)
    led_d.value(1)
    led_e.value(0)
    led_f.value(1)
    led_g.value(1)

def value_six():
    led_a.value(1)
    led_b.value(0)
    led_c.value(1)
    led_d.value(1)
    led_e.value(1)
    led_f.value(1)
    led_g.value(1)

def value_seven():
    led_a.value(1)
    led_b.value(1)
    led_c.value(1)
    led_d.value(0)
    led_e.value(0)
    led_f.value(0)
    led_g.value(0)

def value_eight():
    led_a.value(1)
    led_b.value(1)
    led_c.value(1)
    led_d.value(1)
    led_e.value(1)
    led_f.value(1)
    led_g.value(1)

def value_nine():
    led_a.value(1)
    led_b.value(1)
    led_c.value(1)
    led_d.value(0)
    led_e.value(0)
    led_f.value(1)
    led_g.value(1)

def value_zero():
    led_a.value(1)
    led_b.value(1)
    led_c.value(1)
    led_d.value(1)
    led_e.value(1)
    led_f.value(1)
    led_g.value(0)

# ------------------------------
# Main loop: Show digits 0-9 sequentially
# Each digit is displayed for 1 second
# ------------------------------

while True:
    value_zero()
    time.sleep(1)
    value_one()
    time.sleep(1)
    value_two()
    time.sleep(1)
    value_three()
    time.sleep(1)
    value_four()
    time.sleep(1)
    value_five()
    time.sleep(1)
    value_six()
    time.sleep(1)
    value_seven()
    time.sleep(1)
    value_eight()
    time.sleep(1)
    value_nine()
    time.sleep(1)
