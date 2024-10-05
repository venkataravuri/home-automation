from machine import Pin
from time import sleep

RELAY_PIN = 16
relay = Pin(RELAY_PIN, Pin.OUT)

def solenoid_on():
    relay.value(0)
    
def solenoid_off():
    relay.value(1)

def solenoid_on_off(timer):
    print('Toggle solenoid')
    relay.toggle()

WATER_PUMP_DURATION = 2 * 60 # seconds
WAIT_CYCLE = 150 * 60 # seconds

solenoid_off()

while True:
    solenoid_on()
    print('Solenoid is ON, water is pumping for ' + str(WATER_PUMP_DURATION/60) + ' minutes.')
    sleep(WATER_PUMP_DURATION)
    solenoid_off()
    print('Solenoid is OFF after ' + str(WATER_PUMP_DURATION/60) + ' minutes, water pumping off.')
    print('Next watering cycle is after ' + str(WAIT_CYCLE/(60*60)) + ' hours.')
    sleep(WAIT_CYCLE)
