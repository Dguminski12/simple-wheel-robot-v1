from machine import Pin, PWM
from esp_server import start_server
import time
import network


# Connect to Wi-Fi
ssid = 'EE-NXQ3CM'
password = 'Matura123'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print ("Connecting to Wi-Fi...")

while not wlan.isconnected():
    time.sleep(1)

print("Connected to Wi-Fi. IP address:", wlan.ifconfig()[0])


# GPIO Pins 
AIN1 = Pin(25, Pin.OUT)
AIN2 = Pin(26, Pin.OUT)
PWMA = PWM(Pin(27), freq=1000)

BIN1 = Pin(14, Pin.OUT)
BIN2 = Pin(12, Pin.OUT)
PWMB = PWM(Pin(13), freq=1000)

PWMA.duty(0) # Start with left motor stopped
PWMB.duty(0) # Start with right motor stopped


#Helper Functions

def clamp_speed(speed):
    return max(0, min(1023,speed))

def set_left(dir1, dir2, speed):
    AIN1.value(dir1)
    AIN2.value(dir2)
    PWMA.duty(clamp_speed(speed))

def set_right(dir1, dir2, speed):
    BIN1.value(dir1)
    BIN2.value(dir2)
    PWMB.duty(clamp_speed(speed))

def forward(speed):
    set_left(1, 0, speed)
    set_right(1, 0, speed)

def backward(speed):
    set_left(0, 1, speed)
    set_right(0, 1, speed)

def stop():
    PWMA.duty(0)
    PWMB.duty(0)

def forward_left(speed):
    set_left(1, 0, speed // 2) # Left motor at half speed
    set_right(1, 0, speed) # Right motor at full speed

def forward_right(speed):
    set_left(1, 0, speed)
    set_right(1, 0, speed // 2)

def backward_left(speed):
    set_left(0, 1, speed // 2) # Left motor at half speed
    set_right(0, 1, speed) # Right motor at full speed

def backward_right(speed):
    set_left(0, 1, speed) # Left motor at full speed
    set_right(0, 1, speed // 2) # Right motor at half speed

def left_full(speed):
    set_left(0, 1, speed)
    set_right(1, 0, speed)

def right_full(speed):
    set_left(1, 0, speed)
    set_right(0, 1, speed)

# Command handler for incoming HTTP requests

def handle_command(cmd):

    if cmd == "forward":
        forward(512) # Move forward at 50% speed
    elif cmd == "backward":
        backward(512) # Move backward at 50% speed
    elif cmd == "stop":
        stop() # Stop the robot
    elif cmd == "forward_left":
        forward_left(512) # Move forward and left
    elif cmd == "forward_right":
        forward_right(512) # Move forward and right
    elif cmd == "backward_left":
        backward_left(512) # Move backward and left
    elif cmd == "backward_right":
        backward_right(512) # Move backward and right
    elif cmd == "left_full":
        left_full(512) # Turn left in place
    elif cmd == "right_full":
        right_full(512) # Turn right in place

# Start the HTTP server to listen for commands
start_server(handle_command)

# while True:

#     #Forwards
#     AIN1.on()
#     AIN2.off()
#     PWMA.duty(512) # Set motor speed to 50%
#     time.sleep(2) # Run forward for 2 seconds

#     PWMA.duty(0) # Stop motor
#     time.sleep(1) # Pause for 1 second

#     #Backwards
#     AIN1.off()
#     AIN2.on()
#     PWMA.duty(512) # Set motor speed to 50%
#     time.sleep(2) # Run backward for 2 seconds

#     PWMA.duty(0) # Stop motor
#     time.sleep(1) # Pause for 1 second
