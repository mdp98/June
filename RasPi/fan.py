import RPi.GPIO as GPIO

def on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17,GPIO.OUT)
    print "LED on"
    GPIO.output(17,GPIO.HIGH)

def off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17,GPIO.OUT)
    print "LED off"
    GPIO.output(17,GPIO.LOW)


if __name__ == "__main__":
    main()
