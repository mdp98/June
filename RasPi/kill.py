import RPi.GPIO as GPIO

def killall():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    print "LED off"
    GPIO.output(18,GPIO.LOW)
    GPIO.setup(17,GPIO.OUT)
    print "LED off"
    GPIO.output(17,GPIO.LOW)

    
if __name__=="__main__":
    main()
