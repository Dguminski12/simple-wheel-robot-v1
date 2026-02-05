from machine import Pin, PWM
import time

# GPIO Pins 
AIN1 = Pin(25, Pin.OUT)
AIN2 = Pin(26, Pin.OUT)
PWMA = PWM(Pin(27), freq=1000)

BIN1 = Pin(14, Pin.OUT)
BIN2 = Pin(12, Pin.OUT)
PWMB = PWM(Pin(13), freq=1000)

PWMA.duty(0) # Start with motor stopped

while True:

    #Forwards
    AIN1.on()
    AIN2.off()
    PWMA.duty(512) # Set motor speed to 50%
    time.sleep(2) # Run forward for 2 seconds

    PWMA.duty(0) # Stop motor
    time.sleep(1) # Pause for 1 second

    #Backwards
    AIN1.off()
    AIN2.on()
    PWMA.duty(512) # Set motor speed to 50%
    time.sleep(2) # Run backward for 2 seconds

    PWMA.duty(0) # Stop motor
    time.sleep(1) # Pause for 1 second
