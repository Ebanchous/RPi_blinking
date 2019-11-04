import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(True) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
green = 17
yellow = 27
red = 6
white = 13
ON = False
OFF = True
GPIO.setup(green, GPIO.OUT, initial=GPIO.HIGH) # Set pin 4 to be an output pin and set initial value to low (off)
GPIO.setup(yellow, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(red, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(white, GPIO.OUT, initial=GPIO.HIGH)
for c in range(0,3): # Run forever
    GPIO.output(green, ON) # Turn on
    print("green")
    sleep(0.5) # Sleep for 1 second
    GPIO.output(green, OFF) # Turn off
    sleep(0.3) # Sleep for 1 second
    GPIO.output(yellow, ON) # Turn on
    print("yellow")
    sleep(0.5) # Sleep for 1 second
    GPIO.output(yellow, OFF) # Turn off
    sleep(0.3) # Sleep for 1 second
    GPIO.output(red, ON) # Turn on
    print("red")
    sleep(0.5) # Sleep for 1 second
    GPIO.output(red, OFF) # Turn off
    sleep(0.3) # Sleep for 1 second
    GPIO.output(white, ON) # Turn on
    print("white")
    sleep(0.5) # Sleep for 1 second
    GPIO.output(white, OFF) # Turn off
    sleep(0.3) # Sleep for 1 second 
GPIO.cleanup()
 
