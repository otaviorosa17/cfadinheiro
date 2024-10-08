from libdistancia import HCSR04
from time import sleep

# ESP32
sensor = HCSR04(trigger_pin=12, echo_pin=13, echo_timeout_us=10000)

# ESP8266
#sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)

while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    sleep(0.25)
