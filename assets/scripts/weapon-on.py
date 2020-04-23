# Import required modules
import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins
GPIO.setup(40, GPIO.OUT) # Connected to PWMB
GPIO.setup(36, GPIO.OUT) # Connected to BIN2

# Reset all the GPIO pins by setting them to LOW
GPIO.output(40, GPIO.LOW) # Set PWMB
GPIO.output(36, GPIO.LOW) # Set BIN1

# Drive the motor clockwise
GPIO.output(36, GPIO.HIGH) # Set BIN2

# Set the motor speed
GPIO.output(40, GPIO.HIGH) # Set PWMB
