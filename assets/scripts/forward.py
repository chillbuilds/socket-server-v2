# Import required modules
import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins
GPIO.setup(7, GPIO.OUT) # Connected to PWMA
GPIO.setup(11, GPIO.OUT) # Connected to AIN1
GPIO.setup(13, GPIO.OUT) # Connected to AIN2
GPIO.setup(19, GPIO.OUT) # Connected to PWMB
GPIO.setup(21, GPIO.OUT) # Connected to BIN1
GPIO.setup(23, GPIO.OUT) # Connected to BIN2

# Reset all the GPIO pins by setting them to LOW
GPIO.output(7, GPIO.LOW) # Set PWMA
GPIO.output(11, GPIO.LOW) # Set AIN1
GPIO.output(13, GPIO.LOW) # Set AIN2
GPIO.output(19, GPIO.LOW) # Set PWMB
GPIO.output(21, GPIO.LOW) # Set BIN1
GPIO.output(23, GPIO.LOW) # Set BIN2

# Motor A - Clockwise:
GPIO.output(11, GPIO.LOW) # Set AIN1
GPIO.output(13, GPIO.HIGH) # Set AIN2
# Motor B - Counter Clockwise:
GPIO.output(21, GPIO.LOW) # Set BIN1
GPIO.output(23, GPIO.HIGH) # Set BIN2

# Set the motor speed
# Motor A:
GPIO.output(7, GPIO.HIGH) # Set PWMA
# Motor B:
GPIO.output(19, GPIO.HIGH) # Set PWMB