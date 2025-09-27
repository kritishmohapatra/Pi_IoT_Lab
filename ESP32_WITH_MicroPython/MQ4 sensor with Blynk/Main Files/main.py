import network
import urequests
from machine import ADC, Pin
import time
import gc

# Wi-Fi credentials
SSID = "kritish"
PASSWORD = "@K"

# Blynk token & virtual pin for MQ4
BLYNK_TOKEN = "HVCvifH0WwJe4lDssY6mpULzGy2zhCS"
MQ4_VPIN = "V0"   # Gas gauge

# MQ4 sensor setup
mq4 = ADC(Pin(34))
mq4.atten(ADC.ATTN_11DB)  # Full voltage range
mq4.width(ADC.WIDTH_10BIT)  # 10-bit resolution

# Connect Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)
print("Connecting to WiFi...", end="")
while not wifi.isconnected():
    time.sleep(1)
    print(".", end="")
print("\nConnected to WiFi:", wifi.ifconfig())

def send_to_blynk(vpin, value):
    """Send value to Blynk virtual pin using HTTP"""
    try:
        url = f"http://blynk.cloud/external/api/update?token={BLYNK_TOKEN}&pin={vpin}&value={value}"
        r = urequests.get(url)
        r.close()
    except Exception as e:
        print(f"Error sending {vpin}: {e}")
    finally:
        gc.collect()

def color_coded_gas(value):
    """Cap value 0-1023 for gauge, can add color logic in Blynk widget"""
    return min(max(value, 0), 1023)

while True:
    # Read MQ4
    gas_value = mq4.read()
    voltage = round(gas_value * 3.3 / 1023, 2)

    # Print voltage to serial only
    print(f"MQ4 Gas: {gas_value} | Voltage: {voltage} V")

    # Send color-coded gas value to Blynk gauge
    send_to_blynk(MQ4_VPIN, color_coded_gas(gas_value))

    time.sleep(3)  # 3-second interval

